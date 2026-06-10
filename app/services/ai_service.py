from groq import Groq
import os
import json

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_ai_insight(historical_data):
    prompt = f"""
    You are an admission analytics expert.

    Historical Admission Data:
    {historical_data}

    Return ONLY a JSON object.

    Do not explain.
    Do not provide Python code.
    Do not provide markdown.
    Do not provide text before JSON.
    Do not provide text after JSON.

    Output format:

    {{
      "predicted_admissions": 0,
      "growth_percentage": 0,
      "business_insight": ""
    }}
    """
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )


    content = response.choices[0].message.content

    print("AI RESPONSE =", content)

    return content