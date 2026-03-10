import asyncio
from app.agents.data_agent import analyze_data
from app.agents.insight_agent import generate_insights
from app.agents.report_agent import generate_report


async def run_agents(data: str):

    analysis = await asyncio.to_thread(analyze_data, data)

    insights = await asyncio.to_thread(generate_insights, analysis)

    report = await asyncio.to_thread(generate_report, insights)

    return {
        "analysis": analysis,
        "insights": insights,
        "report": report
    }