import json
from app.services.llm_client import call_llm
from app.services.retriever import retrieve_context


def generate_report(insights):

    context = retrieve_context(str(insights))

    prompt = f"""
You are a senior business consultant.

Use the contextual knowledge below to produce a professional business report.

Context:
{context}

Generate a report.

Return ONLY valid JSON in this format:

{{
 "summary": "",
 "recommendations": []
}}

Insights:
{insights}
"""

    response = call_llm(prompt)

    try:
        result = json.loads(response)
    except:
        result = {
            "raw_output": response
        }

    return result