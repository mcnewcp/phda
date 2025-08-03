"""Test script for the AI Data Logger agent."""

import argparse
import sys
from pathlib import Path

# Add the service directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.agent import create_health_logger_agent
from langchain_core.messages import HumanMessage

def main():
    """Main function to test the health logger agent."""
    parser = argparse.ArgumentParser(description="Test the AI Data Logger agent")
    parser.add_argument(
        "-p", "--prompt",
        type=str,
        help="The prompt to send to the agent",
        default=None
    )
    
    args = parser.parse_args()
    
    # Create the agent
    agent = create_health_logger_agent()
    
    # Use provided prompt or default test prompts
    if args.prompt:
        test_prompts = [args.prompt]
    else:
        test_prompts = [
            "I spent 20 minutes in a 174F sauna at 10:12 am on 2025-07-28",
            "Yesterday at 3pm my blood pressure was 120/80 and heart rate was 65",
            "This morning I weighed 185 lbs with 22% body fat, 85 lbs muscle mass, and 0.38 water ratio",
            "I did a sauna session for 30 minutes this morning and my BP was 118/75 with pulse 70 afterwards"
        ]
    
    for prompt in test_prompts:
        print(f"\n{'='*60}")
        print(f"Testing prompt: {prompt}")
        print('='*60)
        
        result = agent.invoke({
            "messages": [HumanMessage(content=prompt)]
        })
        
        # Print all messages in the conversation
        for msg in result["messages"]:
            if hasattr(msg, 'content'):
                print(f"\n{msg.__class__.__name__}: {msg.content}")
            if hasattr(msg, 'tool_calls') and msg.tool_calls:
                print(f"Tool calls: {msg.tool_calls}")

if __name__ == "__main__":
    main()