from groq import Groq
import os
import json

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def clean_historical_data(historical_data):

    cleaned = []

    for row in historical_data:

        year = row["academic_year"]
        total = row["total"]

        if total <= 20:
            continue

        if year == "8193-8194":
            continue

        # remove abnormal spike
        if total > 1000:
            continue

        cleaned.append(row)

    return cleaned

def generate_ai_insight(historical_data):

    historical_data = clean_historical_data(historical_data)
    print("CLEANED DATA =", historical_data)
    prompt = f"""
    You are an admission analytics expert.

    Historical Admission Data:
    {historical_data}

    Rules:

   1. Use only the provided cleaned data.
   2. Analyze recent admission trends.
   3. Predict next year's admissions.
   4. Return realistic growth percentage.
   5. Return ONLY valid JSON.

    {{
      "predicted_admissions": number,
      "growth_percentage": number,
      "business_insight": "short explanation"
    }}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        temperature=0,
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response.choices[0].message.content

    print("AI RESPONSE =", content)

    return json.loads(content)