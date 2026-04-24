from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

OLLAMA_URL = "http://localhost:11434/api/generate"

@app.post("/ask")
async def ask_llm(user_input: dict):
    """
    Принимает JSON с текстом СМС, отправляет его в Ollama и возвращает ответ.
    
    Args:
        user_input (dict): Словарь с ключом 'text'.
        
    Returns:
        dict: Ответ от языковой модели.
    """
    prompt = user_input.get("text", "")
    if not prompt:
        raise HTTPException(status_code=400, detail="Missing 'text' field")

    payload = {
        "model": "qwen2.5:0.5b",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def health_check():
    """Простая проверка работоспособности сервера."""
    return {"status": "ok", "message": "FastAPI wrapper is running"}