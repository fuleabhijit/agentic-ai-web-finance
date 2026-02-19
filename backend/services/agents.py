import os

from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv


load_dotenv()


def _require_groq_api_key() -> None:
    groq_key = os.getenv("GROQ_API_KEY")
    if not groq_key:
        raise ValueError("GROQ_API_KEY is not set in environment or .env file")
    os.environ["GROQ_API_KEY"] = groq_key


def build_agent_team() -> Agent:
    _require_groq_api_key()

    web_agent = Agent(
        name="Web Agent",
        role="Search the web for information",
        model=Groq(id="llama-3.3-70b-versatile"),
        tools=[DuckDuckGoTools()],
        instructions=(
            "Always include sources at the end. "
            "Use markdown formatting for all output. "
            "For facts and summaries, use bulleted or numbered lists. "
            "Separate each section with a markdown heading (##). "
            "Be concise and structured in your answers."
        ),
        show_tool_calls=False,
        markdown=True,
    )

    finance_agent = Agent(
        name="Finance Agent",
        role="Get financial data",
        model=Groq(id="llama-3.3-70b-versatile"),
        tools=[
            YFinanceTools(
                stock_price=True,
                analyst_recommendations=True,
                stock_fundamentals=True,
                company_info=True,
            )
        ],
        instructions=(
            "Use markdown tables with clear headers for all financial data. "
            "Always include sources at the end. "
            "For analysis, use numbered or bulleted lists. "
            "Separate each section with a markdown heading (##). "
            "Be concise and structured in your answers."
        ),
        show_tool_calls=False,
        markdown=True,
    )

    return Agent(
        team=[web_agent, finance_agent],
        model=Groq(id="llama-3.3-70b-versatile"),
        instructions=[
            "Always include sources at the end.",
            "For financial data, use markdown tables with clear headers.",
            "For analysis, use numbered or bulleted lists.",
            "Separate each section with a markdown heading (##).",
            "Be concise and structured in your answers.",
            "Use markdown formatting for all output.",
        ],
        show_tool_calls=False,
        markdown=True,
    )


def run_analysis(query: str) -> str:
    agent_team = build_agent_team()
    response = agent_team.run(query)
    return getattr(response, "content", str(response))
