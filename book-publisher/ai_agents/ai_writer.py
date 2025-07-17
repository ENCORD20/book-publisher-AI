import ollama

def ai_write(chapter_text, prompt="Rewrite the following chapter in a vivid and engaging literary style:\n\n"):
    full_prompt = prompt + chapter_text
    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": full_prompt}]
    )
    return response['message']['content']