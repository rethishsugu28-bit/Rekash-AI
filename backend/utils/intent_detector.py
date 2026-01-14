def use_multi_ai(question: str) -> bool:
    trigger_words = ["research", "generate", "create"]
    q = question.lower()
    return any(word in q for word in trigger_words)
