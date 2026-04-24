
ollama serve &

echo "Waiting for Ollama to start..."
sleep 5

echo "Downloading Qwen2.5:0.5b model..."
ollama pull qwen2.5:0.5b

echo "Starting FastAPI server..."
uvicorn app.main:app --host 0.0.0.0 --port 8000