from pydantic import BaseModel
from typing import List


class Analysis(BaseModel):
    key_findings: List[str]
    trends: List[str]
    causes: List[str]


class Insights(BaseModel):
    market_implications: List[str]
    opportunities: List[str]


class Report(BaseModel):
    summary: str
    recommendations: List[str]


class AIResponse(BaseModel):
    analysis: Analysis
    insights: Insights
    report: Report