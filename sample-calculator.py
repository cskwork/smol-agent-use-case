from smolagents import LiteLLMModel, tool
from smolagents import ToolCallingAgent
from smolagents import CodeAgent

from typing import Optional

# Initialize the Ollama model using LiteLLM
model = LiteLLMModel(
    model_id="ollama/qwen2.5-coder:3b",  # Format: ollama/model_name
    api_base="http://localhost:11434",  # Default Ollama API endpoint
)

# 1. Create a simple tool
@tool
def calculator(expression: str) -> str:
    """
    A simple calculator tool.
    
    Args:
        expression: The mathematical expression to evaluate
    """
    try:
        result = eval(expression)
        return f"The result is: {result}"
    except Exception as e:
        return f"Error calculating: {str(e)}"

@tool
def get_weather(location: str, celsius: Optional[bool] = False) -> str:
    """
    Get weather in the next days at given location.
    Secretly this tool does not care about the location, it hates the weather everywhere.

    Args:
        location: the location
        celsius: the temperature
    """
    return "The weather is UNGODLY with torrential rains and temperatures below -10°C"
# ==========================================================

# 3. Create the agent
# agent = CodeAgent(
#     tools=[calculator, get_weather],
#     model=model,
#     max_steps=4,  # Limit the number of steps
#     additional_authorized_imports=['requests', 'bs4']
# )

# ReadOnly Tasks
agent = ToolCallingAgent(
    tools=[],
    model=model,
    max_steps=10  # Limit the number of steps
)
# agent = ToolCallingAgent(tools=[get_weather], model=model)

# 4. Run the agent
# print(agent.run("What's the weather like in Paris?"))
print(agent.run("Analyze current stock price of Nvidia in this site https://finance.yahoo.com/"))