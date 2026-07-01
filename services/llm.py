import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_symptoms(patient):
    prompt = f"""
You are an AI Medical Educational Assistant.

Patient Information:
- Name: {patient['name']}
- Age: {patient['age']}
- Gender: {patient['gender']}
- Height: {patient['height']} cm
- Weight: {patient['weight']} kg
- Symptoms: {patient['symptoms']}
- Duration: {patient['duration']}
- Temperature: {patient['temperature']} °C

Based on the above information, provide ONLY the following sections.

## 1. Possible Conditions
- List only 2 to 5 possible conditions.
- Keep each condition to one line.
- Do NOT say the patient definitely has any disease.

## 2. Reasons
- Give only 2 to 5 short bullet points explaining why these conditions may match.

## 3. Home Care
- Give only 2 to 5 simple self-care tips.

## 4. Warning Signs
- Give only 2 to 5 warning signs that require immediate medical attention.

## 5. Recommended Doctor
- Mention only one suitable doctor or specialist.

## 6. Disclaimer
- Write one short sentence stating this is for educational purposes and not a medical diagnosis.

Rules:
- Use simple English.
- Keep the entire response under 250 words.
- Use bullet points only.
- Do not write long paragraphs.
- Do not use markdown tables.
"""

    response = model.generate_content(prompt)

    return response.text