from utils.ollama_client import ask_ollama

def fast_answer(question):
    prompt = f"""
You are Rekash, a smart personal assistant.
Answer clearly and concisely in 4–5 sentences.

Question:
{question}

Answer:
"""
    return ask_ollama(prompt)
