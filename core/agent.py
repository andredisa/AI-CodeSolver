# core/agent.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.google import Gemini

def create_agents():
    vision_agent = Agent(
        model=Gemini(id="gemini-2.0-flash", api_key="your_gemini_api_key"),
        markdown=True
    )

    coding_agent = Agent(
        model=OpenAIChat(id="o3-mini", api_key="your_openai_api_key", system_prompt="..."),
        markdown=True
    )

    execution_agent = Agent(
        model=OpenAIChat(id="o3-mini", api_key="your_openai_api_key", system_prompt="..."),
        markdown=True
    )

    return vision_agent, coding_agent, execution_agent
