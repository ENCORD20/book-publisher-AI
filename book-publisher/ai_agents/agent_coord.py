from . import ai_reviewer
from . import ai_writer


def run_ai_pipeline(chapter_text):
    spun = ai_writer.ai_write(chapter_text)
    reviewed = ai_reviewer.ai_review(spun)
    return reviewed
