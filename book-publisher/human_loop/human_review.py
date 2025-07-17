def human_review_loop(text, max_iter=3):
    for i in range(max_iter):
        print(f"Iteration {i+1} — Current content:\n{text[:200]}...\n")
        new_text = input("Your edits (or press Enter to accept): ")
        if not new_text.strip():
            break
        text = new_text
    return text
