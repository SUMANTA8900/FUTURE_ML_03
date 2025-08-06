from dotenv import load_dotenv
import os
import openai
from backend.vector_search import get_similar_question

# Load from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def fallback_response(user_input):
    prompt = f"Act like a helpful support agent. Answer the following question:\n{user_input}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response["choices"][0]["message"]["content"]

def get_bot_response(user_input):
    answer = get_similar_question(user_input)
    if answer:
        return answer
    else:
        return fallback_response(user_input)
