def analyze_sentiment(text):
    positive_words = ["good", "great", "excellent", "love", "amazing", "best"]
    negative_words = ["bad", "worst", "hate", "poor", "terrible"]

    text = text.lower()

    if any(word in text for word in positive_words):
        return {"label": "POSITIVE", "score": 90}

    if any(word in text for word in negative_words):
        return {"label": "NEGATIVE", "score": 90}

    return {"label": "NEUTRAL", "score": 50}