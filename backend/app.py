from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)  # 🔥 REQUIRED for website to talk to backend

# -------------------------------
# Helper: call Ollama (phi3)
# -------------------------------
def ask_ollama(prompt):
    result = subprocess.run(
        ["ollama", "run", "phi3"],
        input=prompt,
        text=True,
        encoding="utf-8",
        errors="ignore",
        capture_output=True
    )
    return result.stdout.strip()

# -------------------------------
# Intent detector
# -------------------------------
def use_multi_ai(question: str) -> bool:
    trigger_words = ["research", "generate", "create"]
    q = question.lower()
    return any(word in q for word in trigger_words)

# -------------------------------
# Fast personal assistant
# -------------------------------
def fast_answer(question):
    prompt = f"""
You are Rekash, a smart personal assistant.
Answer clearly and concisely.

Question:
{question}

Answer:
"""
    return ask_ollama(prompt)

# -------------------------------
# Multi-AI simulation (same model, different reasoning)
# -------------------------------
def multi_ai_answers(question):
    styles = [
        "Give a simple explanation.",
        "Give a technical explanation.",
        "Give a best-practice focused explanation."
    ]

    answers = []
    for style in styles:
        prompt = f"""
{style}

Question:
{question}

Answer briefly.
"""
        answers.append(ask_ollama(prompt))

    return answers

# -------------------------------
# Judge
# -------------------------------
def judge_and_merge(question, answers):
    prompt = f"""
You are Rekash acting as an AI judge.

Merge the answers below into ONE final,
correct and clear response.

Question:
{question}

Answers:
"""
    for ans in answers:
        prompt += f"\n{ans}\n"

    prompt += "\nFinal Answer:"
    return ask_ollama(prompt)

# -------------------------------
# API Route
# -------------------------------
@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question", "").strip()

    if not question:
        return jsonify({"answer": "Please ask a valid question."})

    if use_multi_ai(question):
        answers = multi_ai_answers(question)
        final_answer = judge_and_merge(question, answers)
    else:
        final_answer = fast_answer(question)

    return jsonify({"answer": final_answer})

# -------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
