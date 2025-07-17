from scraper.wiki_scraper import WikiScraper
from ai_agents.agent_coord import run_ai_pipeline
from human_loop.human_review import human_review_loop
from storage.chromadb_manager import ChromaManager

def main():
    url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
    scraper = WikiScraper(url)
    chapter_text = scraper.fetch_text_and_screenshot(
        out_txt="chapter1.txt", out_png="chapter1.png"
    )

    print("🧠 Running LLaMA 3.2 AI pipeline...")
    ai_spun = run_ai_pipeline(chapter_text)
    final_text = human_review_loop(ai_spun, max_iter=3)

    db = ChromaManager()
    db.add_version(chapter_id="chapter1", text=final_text)
    print("✅ Chapter 1 finalized and stored.")

if __name__ == "__main__":
    main()