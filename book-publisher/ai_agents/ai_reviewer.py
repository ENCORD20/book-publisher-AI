import ollama

def ai_review(text):
    review_prompt = (
        "Review the following chapter for clarity, grammar, and consistency. "
        "Suggest improvements where necessary and present the revised text:\n\n"
    ) + text
    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": review_prompt}]
    )
    return response['message']['content']
