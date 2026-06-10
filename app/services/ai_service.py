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

    Analyze the historical admissions data and predict next year's admissions.

    Return ONLY valid JSON.

    {
    "predicted_admissions": number,
      "growth_percentage": number,
      "business_insight": "short explanation"
    }

    Do not return 0 values.
    Do not return sample data.
    Calculate prediction from the provided historical data.
    Do not return markdown.
    Do not return code.
    Do not return explanations outside JSON.
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