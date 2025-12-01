# app.py
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from agent import analyze_resume

app = FastAPI()

# For HTML templates
templates = Jinja2Templates(directory="templates")

# Optional: serve static files if needed
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "results": None})

@app.post("/analyze", response_class=HTMLResponse)
def analyze(request: Request, resume_text: str = Form(...)):
    result = analyze_resume(resume_text)
    return templates.TemplateResponse("index.html", {"request": request, "results": result})



