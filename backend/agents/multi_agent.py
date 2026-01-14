from utils.ollama_client import ask_ollama

AGENTS = {
    "General": "Give a clear explanation.",
    "Technical": "Give a technically accurate answer.",
    "BestPractices": "Focus on correctness and clarity."
}

def multi_ai_answers(question):
    answers = []
    for style in AGENTS.values():
        prompt = f"""
{style}

Question:
{question}

Answer briefly.
"""
        answers.append(ask_ollama(prompt))
    return answers
