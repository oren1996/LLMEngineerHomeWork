# chatbot.py

import openai
from langchain.memory import ConversationBufferMemory
from langchain.schema import HumanMessage

from config import OPENAI_API_KEY
from create_database import initialize_database
from create_data import add_data
from process_requests import extract_number, extract_order_id, fetch_order_status, process_contact_information

# Initialize LangChain memory
memory = ConversationBufferMemory(return_messages=True)

welcome_message = """Welcome to the Customer Support Chatbot for our E-commerce Platform!
I am here to assist you with the following topics:
1. Order Status: You can check the status of your order.
2. Return Policies: Learn about our different return policies.
3. Human Representative: Request to contact a human representative.

How can I assist you today? Please type your question or request.
"""


enhanced_prompt = """
You are a customer support assistant for an e-commerce platform. Your task is to handle customer support queries related to specific topics.
You should be able to handle multi-turn conversations and provide accurate responses to customer inquiries. Based on the user content and the history of the discussion, determine the type of request and respond appropriately.

Here are the types of requests you can handle and the answer you should return for each type:

1. 'order status' -> Ask the user for their order ID.

2. 'order id' -> Extract the order ID from the user input and output ONLY in this format: "2- The order ID is: "order_id"".
                    BE CAREFUL: The order id might seem like a random string of characters or numbers.

3. 'request human representative' -> If the user asks to talk to a human, superior, or mentions any keywords like "talk to a person," "speak to a manager," or "contact support," ask for their full name, email, phone number.

4. 'contact information' ->  Extract the full name (if present), email address (if present), and phone number (if present) from the user input. Output ALWAYS IN THE FORMAT: "4-" followed by the available information with appropriate labels.
                             For example, if only name is provided, output ONLY IN THIS FORMAT: "4- Name: "name"". If all three are provided, output "4- Name: "name", Email: "email", Phone: "phone"". Ensure the format is correct based on the provided information.

5. 'return policy' -> Output ONLY in this format: "5- return policy".

6. 'non-returnable items' -> Output ONLY in this format: "6- non-returnable items".

7. 'refund process' -> Output ONLY in this format: "7- refund process".

8. 'other' -> Respond politely that you can only assist with specific types of queries.

IMPORTANT: Always maintain a polite and professional tone, providing responses that are direct and easy to understand, ensuring user satisfaction. Your response should reflect the context of the ongoing conversation, adapting as needed based on the user's last input.
"""




# Define a function to get response from OpenAI
def get_openai_response(messages):
    client = openai.OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,
        max_tokens=100,
    )
    return response.choices[0].message.content


# Initialize the chatbot with the initial prompt
def initialize_chatbot():
    initial_messages = [
        {"role": "system", "content": enhanced_prompt}
    ]
    response = get_openai_response(initial_messages)
    # Save the initial prompt and response to memory
    memory.save_context({"input": enhanced_prompt}, {"output": response})
    return response



def chatbot_response(user_input, evaluate_mode=False, mess=None):
    if evaluate_mode:
        messages = []
        initial_context = memory.buffer[:2]
        context = initial_context + mess
        for message in context:
            role = "user" if isinstance(message, HumanMessage) else "assistant"
            messages.append({"role": role, "content": message.content})
        messages.append({"role": "user", "content": user_input})

    else:
        messages = []
        initial_context = memory.buffer[:2]
        last_9_pairs = memory.buffer[-8:]
        context = initial_context + last_9_pairs
        for message in context:
            role = "user" if isinstance(message, HumanMessage) else "assistant"
            messages.append({"role": role, "content": message.content})
        messages.append({"role": "user", "content": user_input})

    # Get response from OpenAI
    answer = get_openai_response(messages)
    number = extract_number(answer)

    if number == 2:
        order_id = extract_order_id(answer)
        if order_id is None:
            answer = "Your order ID was not found, it might be misspelled so please check the order ID and try again."
        else:
            answer = fetch_order_status(order_id)

    elif number == 4:
        answer = process_contact_information(answer)

    elif number == 5:
        answer = "You can return most items within 30 days of purchase for a full refund or exchange. Items must be in their original condition, with all tags and packaging intact. Please bring your receipt or proof of purchase when returning items.\nIs there anything else I can do ?"

    elif number == 6:
        answer = "Yes, certain items such as clearance merchandise, perishable goods, and personal care items are non-returnable. Please check the product description or ask a store associate for more details.\nIs there anything else I can do ?"

    elif number == 7:
        answer = "Refunds will be issued to the original form of payment. If you paid by credit card, the refund will be credited to your card. If you paid by cash or check, you will receive a cash refund.\nIs there anything else I can do ?"


# Update the context with the user input and the response
    memory.save_context({"input": user_input}, {"output": answer})
    return answer


def main():
    initialize_database()
    add_data()
    initialize_chatbot()

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        chatbot_response(user_input)


if __name__ == "__main__":
    main()

