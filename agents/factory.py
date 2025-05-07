from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.google import Gemini
import streamlit as st

def create_agents():
    vision_agent = Agent(
        model=Gemini(id="gemini-2.0-flash", api_key=st.session_state.gemini_key),
        markdown=True,
    )

    coding_agent = Agent(
        model=OpenAIChat(
            id="o3-mini",
            api_key=st.session_state.openai_key,
            system_prompt="""You are an expert Python programmer..."""
        ),
        markdown=True
    )

    execution_agent = Agent(
        model=OpenAIChat(
            id="o3-mini",
            api_key=st.session_state.openai_key,
            system_prompt="""You are an expert at executing Python code..."""
        ),
        markdown=True
    )

    return vision_agent, coding_agent, execution_agent
