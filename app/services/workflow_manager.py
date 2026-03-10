from app.agents.data_agent import analyze_data
from app.agents.insight_agent import generate_insights
from app.agents.report_agent import generate_report

def run_workflow(data: str):
    
    analysis = analyze_data(data)
    
    insights = generate_insights(analysis)
    
    report = generate_report(insights)

    return {
        "analysis": analysis,
        "insights": insights,
        "report": report
    }