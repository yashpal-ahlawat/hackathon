import requests
from config import OLLAMA_API_URL

def generate_response(prompt, context):
    system_prompt = f"""Use the following context to answer the question. 
    If you cannot find the answer in the context, say so.
    
    Context: {context}
    
    Question: {prompt}
    """
    
    response = requests.post(
        OLLAMA_API_URL,
        json={
            "model": "deepseek-r1:1.5b",
            "prompt": system_prompt,
            "stream": False
        }
    )
    if response.status_code == 200:
        return response.json()['response']
    else:
        return "Error generating response"