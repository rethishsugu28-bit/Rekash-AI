from utils.ollama_client import ask_ollama

def judge_and_merge(question, answers):
    prompt = f"""
You are Rekash, acting as an AI judge.

Merge the answers below into ONE correct,
clean final response.

Question:
{question}

Answers:
"""
    for ans in answers:
        prompt += f"\n{ans}\n"

    prompt += "\nFinal Answer:"
    return ask_ollama(prompt)
