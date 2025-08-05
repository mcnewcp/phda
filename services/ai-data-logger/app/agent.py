import os
from phoenix.otel import register

from typing import Annotated

from typing_extensions import TypedDict
from pydantic import SecretStr

from datetime import datetime
import pytz

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from langchain_core.messages import SystemMessage
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI

from tools.health_log_tools import log_heart_data, log_body_data, log_sauna_data

# instrument to phoenix
# Use environment variable if set, fallback to localhost for development
phoenix_endpoint = os.environ.get("PHOENIX_COLLECTOR_ENDPOINT", "http://localhost:4317")
tracer_provider = register(
    project_name="ai-data-logger",
    endpoint=phoenix_endpoint,
    auto_instrument=True
)

#### SYSTEM PROMPT #####
def get_current_time_prompt():
    """Generate system prompt with current time."""
    central_tz = pytz.timezone('US/Central')
    current_time = datetime.now(central_tz)
    
    return f"""You are a health data logging assistant. Your job is to parse natural language health tracking inputs and log them to the appropriate database tables.

Current date and time: {current_time.strftime('%Y-%m-%d %H:%M:%S %Z')}

Available logging tools:
- log_heart_data: For blood pressure and heart rate (requires systolic, diastolic, heart rate)
- log_body_data: For body composition (requires weight, muscle mass, body fat %, water ratio)
- log_sauna_data: For sauna sessions (requires duration in minutes; temperature in Fahrenheit is optional)

Important guidelines:
1. Parse datetime references carefully. Examples:
   - "yesterday at 3pm" -> calculate from current time
   - "this morning" -> today at a reasonable morning time
   - "an hour ago" -> subtract 1 hour from current time
2. All times should be in Central Time (US/Central)
3. If information is missing or unclear, ask for clarification
4. After logging, summarize what was recorded
5. Handle multiple entries in a single prompt appropriately
"""

#### BUILD GRAPH #####

# graph state
class State(TypedDict):
    # Messages have the type "list". The `add_messages` function
    # in the annotation defines how this state key should be updated
    # (in this case, it appends messages to the list, rather than overwriting them)
    messages: Annotated[list, add_messages]

# LLM provider factory
def get_llm_model():
    """Get the configured LLM model based on environment variable."""
    provider = os.environ.get("LLM_PROVIDER", "ollama").lower()
    
    if provider == "openai":
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable is required when using OpenAI provider")
        return ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0,
            api_key=SecretStr(api_key)
        )
    elif provider == "ollama":
        return ChatOllama(
            model="qwen2.5:7b",
            temperature=0,
            base_url="http://host.docker.internal:11434"
        )
    else:
        raise ValueError(f"Unsupported LLM provider: {provider}")

# nodes
def call_model(state: State):
    # Initialize model with tools
    model = get_llm_model()
    tools = [log_heart_data, log_body_data, log_sauna_data]
    model_with_tools = model.bind_tools(tools)

    # build messages
    messages = state["messages"]
    # Add system prompt with current time
    messages_with_system = [
        SystemMessage(content=get_current_time_prompt()),
        *messages
    ]

    response = model_with_tools.invoke(messages_with_system)
    return {"messages": [response]}

def should_continue(state: State):
    """Determine if we should continue to tools or end."""
    messages = state["messages"]
    last_message = messages[-1]
    
    # If the LLM wants to use tools, route to tool node
    if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
        return "tools"
    # Otherwise we're done
    return END

def create_health_logger_agent():
    """Create the health logger agent graph."""
    # Initialize the graph
    graph_builder = StateGraph(State)
    
    # Define the tools
    tools = [log_heart_data, log_body_data, log_sauna_data]
    tool_node = ToolNode(tools)
    
    # Add nodes
    graph_builder.add_node("agent", call_model)
    graph_builder.add_node("tools", tool_node)
    
    # Set entry point
    graph_builder.add_edge(START, "agent")
    
    # Add conditional edges
    graph_builder.add_conditional_edges(
        "agent",
        should_continue,
        {
            "tools": "tools",
            END: END
        }
    )
    
    # Always return to agent after tool execution
    graph_builder.add_edge("tools", "agent")
    
    # Compile the graph
    return graph_builder.compile()