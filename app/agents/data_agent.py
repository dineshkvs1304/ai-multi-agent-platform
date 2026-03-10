import json
from app.services.llm_client import call_llm
from app.services.retriever import retrieve_context


def analyze_data(data: str):

    context = retrieve_context(data)

    prompt = f"""
You are a professional business analyst.

Use the following context to improve the analysis.

Context:
{context}

Analyze the business data.

Return JSON:

{{
 "key_findings": [],
 "trends": [],
 "causes": []
}}

Data:
{data}
"""

    response = call_llm(prompt)

    try:
        result = json.loads(response)
    except:
        result = {"raw_output": response}

    return result