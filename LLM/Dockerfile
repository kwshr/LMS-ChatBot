FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Set PYTHONPATH to include your module directories
ENV PYTHONPATH=/app/LLM/Data_Objects:/app/LLM/Model:/app/LLM/TextGeneration:/app/LLM/Train:/app/LLM/GPT_weights

EXPOSE 5000

ENV FLASK_APP=main.py

CMD ["flask", "run", "--host=0.0.0.0"]