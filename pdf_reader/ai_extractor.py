import os
import requests

def extract_car_info(text):
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    prompt = f"""
You will be given a car insurance claim report. Extract and return the following details in HTML bullet points:
• Car Name
• Car Model (e.g., 2018, 2021)
• Policy Holder
• License Plate
• Damage Location
• Based on the damage location, what parts should be inspected?

Report:
{text}
"""

    data = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
    try:
        return response.json()['choices'][0]['message']['content']
    except:
        return "Could not extract information. Check the API response."