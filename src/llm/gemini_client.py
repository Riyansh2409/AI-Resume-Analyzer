import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv(override=True)

api_key = os.getenv("GEMINI_API_KEY")


if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_response(prompt):
    response = model.generate_content(prompt)
    return response.text