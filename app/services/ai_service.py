from groq import Groq
import os
import json

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
def generate_ai_insight(prediction):

    prompt = f"""
    You are an admission analytics expert.

    Prediction Result:

    Predicted Admissions: {prediction["predicted_admissions"]}

    Growth Status: {prediction["growth_status"]}

    Rules:

    1. Do not mention percentages.
    2. Do not mention decline or negative growth.
    3. Generate a positive and professional business insight.
    4. Keep it to one sentence.
    5. Return ONLY valid JSON.

    {{
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