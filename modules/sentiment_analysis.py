import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER lexicon (only once)
nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

def analyze_sentiment(answer_text):
    """
    Analyze sentiment of interview answer using VADER
    """

    if answer_text.strip() == "":
        return "NEUTRAL", 0.0

    scores = sia.polarity_scores(answer_text)
    compound = scores["compound"]

    if compound >= 0.05:
        return "POSITIVE", compound
    elif compound <= -0.05:
        return "NEGATIVE", compound
    else:
        return "NEUTRAL", compound
