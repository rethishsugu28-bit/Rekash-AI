from flask import Flask, request, jsonify
from utils.intent_detector import use_multi_ai
from agents.fast_assistant import fast_answer
from agents.multi_agent import multi_ai_answers
from judge.judge import judge_and_merge

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)
