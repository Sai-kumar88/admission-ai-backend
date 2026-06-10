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

    Rules:
    1. Use the admission data provided only.
    2. Analyze admission trends using previous academic years.
    3. Predict next year's admissions realistically.
    4. Do NOT generate extreme growth percentages.
    5. Do NOT invent data that is not supported by the historical data.
    6. If the trend is uncertain, provide a conservative prediction.
    7. The predicted admissions should be reasonably close to recent academic years.
    8. Return valid JSON only.

    Return ONLY:

    {{
        "predicted_admissions": number,
        "growth_percentage": number,
        "business_insight": "short business explanation"
    }}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response.choices[0].message.content

    return json.loads(content)