# agent.py
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env values
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not found in .env")

# Configure Gemini
genai.configure(api_key=API_KEY)

# Choose recommended model
MODEL_NAME = "gemini-1.5-flash"

def analyze_resume(resume_text):
    prompt = f"""
You are an expert resume evaluator. Analyze the following resume text and provide:

1. Top Skills (bullet points)
2. Suggested Improvements (bullet points)
3. ATS Score (0–100)
4. Cover Letter Bullets (2–3 points)

Resume:
{resume_text}
"""

    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"❌ Error: {str(e)}"









