import json
from app.services.llm_client import call_llm
from app.services.retriever import retrieve_context


def generate_insights(analysis):

    context = retrieve_context(str(analysis))

    prompt = f"""
You are a senior business strategy expert.

Use the following contextual business knowledge to improve your insights.

Context:
{context}

Generate strategic insights based on the analysis.

Return ONLY valid JSON in this format:

{{
 "market_implications": [],
 "opportunities": []
}}

Analysis:
{analysis}
"""

    response = call_llm(prompt)

    try:
        result = json.loads(response)
    except:
        result = {
            "raw_output": response
        }

    return result