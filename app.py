from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from agents.classifier import classify_intent
from agents.generator import generate_response
from agents.escalation import handle_escalation

load_dotenv()

app = FastAPI(
    title="Multi-Agent Customer Support",
    description="AI-powered multi-agent customer support system using RAG",
    version="1.0.0"
)

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    intent: str
    response: str

@app.get("/")
def home():
    return {
        "message": "Multi-Agent Customer Support API is running",
        "docs": "/docs"
    }

@app.post("/chat", response_model=QueryResponse)
def chat(request: QueryRequest):
    query = request.query

    # Step 1: Classify Intent
    intent = classify_intent(query)

    # Step 2: Route to Escalation or Generator
    if intent == "escalate":
        answer = handle_escalation(query)
    else:
        answer = generate_response(query)

    return {
        "intent": intent,
        "response": answer
    }
