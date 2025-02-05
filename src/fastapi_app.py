from fastapi import FastAPI, HTTPException
from database import fetch_relevant_data
from ollama_client import generate_response
from models import Query, Response
import uvicorn

app = FastAPI(title="RAG API", description="API for RAG-powered insights generation")

@app.post("/api/query", response_model=Response)
async def query(query_data: Query):
    if not query_data.query:
        raise HTTPException(status_code=400, detail="No query provided")
    
    # Fetch relevant context from database
    # context = fetch_relevant_data(query_data.query)
    context = "you are an ai assistant to help me with my queries".split()
    # Generate response using Ollama
    response = generate_response(query_data.query, "\n".join(context))
    
    return Response(response=response, context=context)

if __name__ == '__main__':
    uvicorn.run("fastapi_app:app", host="0.0.0.0", port=8000, reload=True)
