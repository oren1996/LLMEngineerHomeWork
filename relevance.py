import chatbot

def evaluate_relevance():
    predefined_dialogues = [

        ### asking for order status with order ID that exists
        {
            "user_input": "What is the status of my order?",
            "expected_response": "I can help with that. Could you please provide me with your order ID?"
        },
        {
            "user_input": "The order ID is: 011",
            "expected_response": "For your order ID 011, the status is Delivered.\nIs there anything else I can do ?"
        },

        ### asking for order status with order ID that does not exist
        {
            "user_input": "What is the status of my order?",
            "expected_response": "I can help with that. Could you please provide me with your order ID?"
        },
        {
            "user_input": "The order ID is: 030",
            "expected_response": "Your order ID 030 was not found, it might be misspelled so please check the order ID and try again."
        },

        ### asking for contact information with correct format given
        {
            "user_input": "I want to talk to a human representative.",
            "expected_response": "Sure, I can assist you with that. Could you please provide me with your full name, email address, and phone number?"
        },
        {
            "user_input": "Joe Yang, joeyang@example.com, 001-671-370-7753x174",
            "expected_response": "Contact information saved successfully. Is there anything else i can do ?"
        },

        ### asking for contact information with incorrect format given
        {
            "user_input": "I want to talk to a human representative.",
            "expected_response": "Sure, I can assist you with that. Could you please provide me with your full name, email address, and phone number?"
        },
        {
            "user_input": "joeyang@example.com, 001-671-370-7753x174",
            "expected_response": "I'm sorry, but I need your full name, email, and phone number to connect you with a human representative. Can you please provide that information?"
        },


        ### asking for return policy
        {
            "user_input": "What is the return policy for items purchased at your store?",
            "expected_response": "You can return most items within 30 days of purchase for a full refund or exchange. Items must be in their original condition, with all tags and packaging intact. Please bring your receipt or proof of purchase when returning items.\nIs there anything else I can do ?"
        },

        ### asking for return policy details
        {
            "user_input": "Are there any items that cannot be returned under this policy?",
            "expected_response": "Yes, certain items such as clearance merchandise, perishable goods, and personal care items are non-returnable. Please check the product description or ask a store associate for more details.\nIs there anything else I can do ?"
        },

        ### asking for refund details
        {
            "user_input": "How will I receive my refund?",
            "expected_response": "Refunds will be issued to the original form of payment. If you paid by credit card, the refund will be credited to your card. If you paid by cash or check, you will receive a cash refund.\nIs there anything else I can do ?"
        },

    ]

    relevance_scores = []

    for dialogue in predefined_dialogues:
        user_input = dialogue['user_input']
        expected_response = dialogue['expected_response']
        actual_response = chatbot.chatbot_response(user_input)
        print(f"User: {user_input}")
        print(f"Bot: {actual_response}")
        print(f"Expected: {expected_response}")

        score = int(input("Rate the relevance of this response (1 to 5): "))
        relevance_scores.append(score)

    average_relevance = sum(relevance_scores) / len(relevance_scores)
    return average_relevance

