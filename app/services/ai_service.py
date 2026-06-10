from groq import Groq
import os
import json

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def calculate_prediction(historical_data):

    values = []

    for row in historical_data:
        if row["total"] > 20:
            values.append(row["total"])

    recent = values[-3:]

    predicted = round(sum(recent) / len(recent))

    growth = round(
        ((predicted - recent[-1]) / recent[-1]) * 100,
        2
    )

    return {
        "predicted_admissions": predicted,
        "growth_percentage": growth
    }


def generate_ai_insight(historical_data):
    prompt = f"""
    You are an admission analytics expert.

    Historical Admission Data:
    {historical_data}

    Analyze the historical admissions data and predict next year's admissions.

    Return ONLY valid JSON.

   {{
  "predicted_admissions": number,
  "growth_percentage": number,
  "business_insight": "short explanation"
   }}

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