import google.generativeai as genai
import os

# Load API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def analyze_resume(resume_text):
    prompt = f"""
    You are an ATS Resume Analyzer.
    Analyze this resume and give results in the following format only:

    ### Results
    Brief summary.

    ### Top Skills
    List top 5 skills.

    ### Suggested Improvements
    5 bullet points.

    ### Cover Letter Bullets
    3 short bullets.

    ### ATS Score
    Score out of 100.

    Resume:
    {resume_text}
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"








