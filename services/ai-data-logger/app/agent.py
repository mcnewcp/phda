import os
from phoenix.otel import register

from typing import Annotated

from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_ollama import ChatOllama

# instrument to phoenix
# Use environment variable if set, fallback to localhost for development
phoenix_endpoint = os.environ.get("PHOENIX_COLLECTOR_ENDPOINT", "http://localhost:4317")
tracer_provider = register(
    project_name="ai-data-logger",
    endpoint=phoenix_endpoint,
    auto_instrument=True
)

#### BUILD GRAPH #####

# graph state
class State(TypedDict):
    # Messages have the type "list". The `add_messages` function
    # in the annotation defines how this state key should be updated
    # (in this case, it appends messages to the list, rather than overwriting them)
    messages: Annotated[list, add_messages]

# nodes
def chatbot(state: State):
    # Initialize model with tools
    # Use host.docker.internal to connect to Ollama running on host machine
    model = ChatOllama(
        model = "qwen2.5:7b",
        temperature = 0,
        base_url = "http://host.docker.internal:11434"
    )

    return {"messages": [model.invoke(state["messages"])]}

def create_health_logger_agent():
    """Create the health logger agent graph."""
    # Initialize the graph
    graph_builder = StateGraph(State)
    
    # Define the tools
    # tools = [log_heart_data, log_body_data, log_sauna_data]
    # tool_node = ToolNode(tools)
    
    # Add nodes
    graph_builder.add_node("chatbot", chatbot)
    # workflow.add_node("tools", tool_node)
    
    # Set entry point
    graph_builder.add_edge(START, "chatbot")
    graph_builder.add_edge("chatbot", END)
    
    # Add conditional edges
    # workflow.add_conditional_edges(
    #     "agent",
    #     should_continue,
    #     {
    #         "tools": "tools",
    #         END: END
    #     }
    # )
    
    # Always return to agent after tool execution
    # workflow.add_edge("tools", "agent")
    
    # Compile the graph
    return graph_builder.compile()