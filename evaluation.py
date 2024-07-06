from accuracy import evaluate_accuracy
from user_satisfaction import evaluate_user_satisfaction
from relevance import evaluate_relevance

def main():
    final_accuracy = evaluate_accuracy()
    # final_relevance = evaluate_relevance()
    # final_rating, final_sentiment = evaluate_user_satisfaction()

    # Calculate and print accuracy
    print(f"Accuracy: {final_accuracy:.2f}%")

    # Calculate and print average relevance rating
    # print(f"Average Relevance Rating: {final_relevance:.2f}/5")

    # Calculate and print average relevance rating
    # print(f"Average User Rating: {final_rating:.2f}")
    # print(f"Average Sentiment: {final_sentiment:.2f}")


if __name__ == "__main__":
    main()