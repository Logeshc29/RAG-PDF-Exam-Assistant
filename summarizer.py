from transformers import pipeline

def summarize_text(text):

    summarizer = pipeline(
        "summarization",
        model="facebook/bart-large-cnn"
    )

    result = summarizer(
        text[:1000]
    )

    return result[0]['summary_text']
