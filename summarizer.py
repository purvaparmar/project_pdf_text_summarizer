import PyPDF2
from transformers import pipeline
from keybert import KeyBERT
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, max_length=130, min_length=30):
    max_chunk = 1000
    chunks = [text[i:i+max_chunk] for i in range(0, len(text), max_chunk)]
    summary = ""

    for chunk in chunks:
        res = summarizer(chunk, max_length=max_length, min_length=min_length, do_sample=False)
        summary += res[0]['summary_text'] + " "

    return summary.strip()
def extract_keywords(text, top_n=5):
    kw_model = KeyBERT()
    keywords = kw_model.extract_keywords(text, top_n=top_n)
    return [kw[0] for kw in keywords]