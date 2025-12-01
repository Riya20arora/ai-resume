# agent.py
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY")
if not HF_API_KEY:
    raise ValueError("❌ HF_API_KEY not set in .env")

# Model to use
MODEL_NAME = "tiiuae/falcon-7b-instruct"

# Initialize Hugging Face inference client
inference = InferenceClient(token=HF_API_KEY)

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
        response = inference.text_generation(model=MODEL_NAME, inputs=prompt)
        return response.generated_text
    except Exception:
        # fallback mock data
        return {
            "summary": "Sample summary: This is a demo analysis.",
            "skills": ["Python", "Machine Learning", "Data Analysis"],
            "improvements": ["Make resume more concise", "Highlight achievements"],
            "cover_bullets": ["Bullet 1", "Bullet 2", "Bullet 3"],
            "ats_score": 85
        }






