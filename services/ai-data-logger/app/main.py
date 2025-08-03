from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any, Literal
from .agent import create_health_logger_agent
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="AI Data Logger", version="1.0.0")

# Initialize agent with error handling
try:
    agent = create_health_logger_agent()
    logger.info("Health logger agent initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize agent: {str(e)}")
    raise RuntimeError(f"Failed to initialize agent: {str(e)}")

class Message(BaseModel):
    role: Literal["user", "assistant"]
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]

class ChatResponse(BaseModel):
    message: Message
    logged_items: List[Dict[str, Any]] = []

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "ai-data-logger"}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Process a conversation with the health tracking assistant.
    
    Args:
        request: Contains the conversation history
        
    Returns:
        ChatResponse with the assistant's response and any logged items
    """
    try:
        # Convert request messages to LangChain format
        langchain_messages = []
        for msg in request.messages:
            if msg.role == "user":
                langchain_messages.append(HumanMessage(content=msg.content))
            else:
                langchain_messages.append(AIMessage(content=msg.content))
        
        logger.info(f"Processing chat with {len(langchain_messages)} messages")
        
        # Invoke the agent
        result = agent.invoke({"messages": langchain_messages})
        
        # Extract the final AI message
        final_message = result["messages"][-1]
        
        # Parse tool calls to extract logged items
        logged_items = []
        for msg in result["messages"]:
            if isinstance(msg, ToolMessage):
                # Parse the tool message content to extract logged data
                # This is a simplified version - in production you'd parse more carefully
                content_str = str(msg.content)
                if "success" in content_str and "true" in content_str.lower():
                    logged_items.append({
                        "tool": msg.name,
                        "result": msg.content
                    })
        
        return ChatResponse(
            message=Message(
                role="assistant",
                content=final_message.content
            ),
            logged_items=logged_items
        )
        
    except Exception as e:
        logger.error(f"Error in chat endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))