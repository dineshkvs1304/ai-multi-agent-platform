import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL = "llama-3.1-8b-instant"  # fast & free on Groq


def call_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are an expert business analyst."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=500,
    )

    return response.choices[0].message.content