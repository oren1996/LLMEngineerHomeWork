from textblob import TextBlob
import chatbot

def get_user_feedback():
    rating = int(input("Please rate this conversation on a scale of 1 to 5: "))
    comments = input("Any additional comments? ")
    return rating, comments

def analyze_sentiment(comments):
    analysis = TextBlob(comments)
    return analysis.sentiment.polarity

def evaluate_user_satisfaction():
    rating, comments = get_user_feedback()
    average_rating = rating
    average_sentiment = analyze_sentiment(comments)
    return average_rating, average_sentiment

    # Positive Sentiment: Scores close to 1 indicate that the text expresses a positive sentiment.
    # Negative Sentiment: Scores close to -1 indicate that the text expresses a negative sentiment.
    # Neutral Sentiment: Scores around 0 indicate that the text is neutral.


