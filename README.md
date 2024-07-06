# Conversational Agent for E-commerce Platform

## Description
This project implements a conversational agent (chatbot) using the OpenAI API to handle customer support queries for an e-commerce platform.

## Features
- Order Status: Provides the status of an order.
- Return Policies: Information about the return policies.
- Request Human Representative: Collects contact information for users wanting to interact with a human representative.

## Running and Testing the Agent


### Environment Setup
1. Clone the repository.
2. Navigate to the project directory.
3. Create a virtual environment:
   ```bash
   conda create -n chatbot python=3.8
   ```
4. Activate the virtual environment:
   ```bash
    conda activate chatbot
    ```
5. Configure the OpenAI API key
   

### Running the Agent:
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the database setup:
   ```bash
   python create_database.py
   ```
3. Add mock data:
   ```bash
   python create_data.py
   ```
4. Start the chatbot server:
   ```bash
   streamlit run app.py
   ```


## Evaluation
Run the evaluation script to test the chatbot's accuracy.
   ```bash
   streamlit run evaluation.py
   ```

## Note
If you want to check the relevance of the chatbot's responses or the user satisfaction, go to the evaluation.py file and comment out those lines: <br>
1) lines 8 and 9:
```python
# final_rating, final_sentiment = evaluate_user_satisfaction()
# final_relevance = evaluate_relevance()
```

2) lines 15, 18 and 19:
```python
# Calculate and print average relevance rating
# print(f"Average Relevance Rating: {final_relevance:.2f}/5")

# Calculate and print average relevance rating
# print(f"Average User Rating: {final_rating:.2f}")
# print(f"Average Sentiment: {final_sentiment:.2f}")
```

then run the evaluation script again and follow the instructions.