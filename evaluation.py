# evaluation.py

import chatbot
import process_requests
import csv
import random
import sqlite3
from faker import Faker
import os
from chatbot import enhanced_prompt


class HumanMessage:
    def __init__(self, content):
        self.role = "user"
        self.content = content


class AIMessage:
    def __init__(self, content):
        self.role = "assistant"
        self.content = content


# Initialize counters for accuracy calculation
total_tests = 0
successful_tests = 0


def evaluate_status_order():
    global total_tests, successful_tests
    total_tests += 1

    status_order_questions = {"user_input": "What is the status of my order?",
                              "expected_key_words": ["order ID"]}
    response = chatbot.chatbot_response(status_order_questions["user_input"])

    print(f"User: {status_order_questions['user_input']}")
    print(f"Bot: {response}")
    print(f"Expected Key words in response: {status_order_questions['expected_key_words']}")

    key_words = status_order_questions['expected_key_words']
    for key_word in key_words:
        if key_word not in response:
            print(f"Match: False\n")
            return
    successful_tests += 1
    print(f"Match: True\n")


def generate_order_id():
    outcomes = ['range1', 'range2']
    weights = [1 / 2, 1 / 2]
    choice = random.choices(outcomes, weights)[0]
    if choice == 'range1':
        random_number = random.randint(1, 16)
        order_id = f"{random_number:03}"
    else:
        random_number = random.randint(17, 30)
        order_id = f"{random_number:03}"
    return order_id


def create_status_id_questions():
    global total_tests, successful_tests
    total_tests += 1

    ask_order_id = [
        HumanMessage(content="What is the status of my order?"),
        AIMessage(content="Please provide your order ID to check the status.")
    ]

    conn = sqlite3.connect('ecommerce.db')
    c = conn.cursor()
    status_id_questions = {}
    order_id = generate_order_id()
    status_id_questions["user_input"] = f"The order ID is: {order_id}"
    good_range = ["001", "002", "003", "004", "005", "006", "007", "008", "009", "010", "011", "012", "013", "014",
                  "015", "016"]
    bad_range = ["017", "018", "019", "020", "021", "022", "023", "024", "025", "026", "027", "028", "029", "030"]
    if order_id in good_range:
        c.execute('SELECT status FROM Orders WHERE order_id = ?', (order_id,))
        order = c.fetchone()
        if order:
            order_status = order[0]
            status_id_questions["expected_response"] = f"For your order ID {order_id}, the status is {order_status}"
        else:
            status_id_questions[
                "expected_response"] = "Your order ID was not found, it might be misspelled so please check the order ID and try again."
    elif order_id in bad_range:
        status_id_questions[
            "expected_response"] = f"Your order ID {order_id} was not found, it might be misspelled so please check the order ID and try again."

    conn.close()
    response = chatbot.chatbot_response(status_id_questions["user_input"], evaluate_mode=True, mess=ask_order_id)
    print(f"User: What is the status of my order?")
    print(f"Bot: Please provide your order ID to check the status.")
    print(f"User: {status_id_questions['user_input']}")
    print(f"Bot: {response}")
    print(f"Expected: {status_id_questions['expected_response']}")
    print(f"Match: {status_id_questions['expected_response'] in response}\n")
    if status_id_questions['expected_response'] in response:
        successful_tests += 1


def evaluate_return_policy():
    global total_tests, successful_tests
    total_tests += 1

    return_policy_question = {"user_input": "What is the return policy for items purchased at your store?",
                              "expected_response": "You can return most items within 30 days of purchase for a full refund or exchange. Items must be in their original condition, with all tags and packaging intact. Please bring your receipt or proof of purchase when returning items.\nIs there anything else I can do ?"}
    response = chatbot.chatbot_response(return_policy_question["user_input"])
    print(f"User: {return_policy_question['user_input']}")
    print(f"Bot: {response}")
    print(f"Expected: {return_policy_question['expected_response']}")
    print(f"Match: {return_policy_question['expected_response'] in response}\n")
    if return_policy_question['expected_response'] in response:
        successful_tests += 1


def evaluate_non_returnable_items():
    global total_tests, successful_tests
    total_tests += 1

    non_returnable_items_question = {"user_input": "Are there any items that cannot be returned under this policy?",
                                     "expected_response": "Yes, certain items such as clearance merchandise, perishable goods, and personal care items are non-returnable. Please check the product description or ask a store associate for more details.\nIs there anything else I can do ?"}
    response = chatbot.chatbot_response(non_returnable_items_question["user_input"])
    print(f"User: {non_returnable_items_question['user_input']}")
    print(f"Bot: {response}")
    print(f"Expected: {non_returnable_items_question['expected_response']}")
    print(f"Match: {non_returnable_items_question['expected_response'] in response}\n")
    if non_returnable_items_question['expected_response'] in response:
        successful_tests += 1


def evaluate_refund_process():
    global total_tests, successful_tests
    total_tests += 1

    refund_process_question = {"user_input": "How will I receive my refund?",
                               "expected_response": "Refunds will be issued to the original form of payment. If you paid by credit card, the refund will be credited to your card. If you paid by cash or check, you will receive a cash refund.\nIs there anything else I can do ?"}
    response = chatbot.chatbot_response(refund_process_question["user_input"])
    print(f"User: {refund_process_question['user_input']}")
    print(f"Bot: {response}")
    print(f"Expected: {refund_process_question['expected_response']}")
    print(f"Match: {refund_process_question['expected_response'] in response}\n")
    if refund_process_question['expected_response'] in response:
        successful_tests += 1


def evaluate_request_human_representative():
    global total_tests, successful_tests
    total_tests += 1

    human_representative_question = {"user_input": "I want to talk to a human representative.",
                                     "expected_key_words": ["provide", "full name", "email", "number"]}
    response = chatbot.chatbot_response(human_representative_question["user_input"])
    print(f"User: {human_representative_question['user_input']}")
    print(f"Bot: {response}")
    print(f"Expected Key words in response: {human_representative_question['expected_key_words']}")
    key_words = human_representative_question['expected_key_words']
    for key_word in key_words:
        if key_word not in response:
            print(f"Match: False\n")
            return
    successful_tests += 1
    print(f"Match: True\n")


def generate_random_contact_info(scenario_num):
    fake = Faker()
    contact_info = {'full_name': fake.name(),
                    'email': fake.email(),
                    'phone_number': fake.phone_number()}

    scenarios = [
        {'full_name': contact_info['full_name'], 'email': None, 'phone_number': None},
        {'full_name': None, 'email': contact_info['email'], 'phone_number': None},
        {'full_name': None, 'email': None, 'phone_number': contact_info['phone_number']},
        {'full_name': contact_info['full_name'], 'email': contact_info['email'], 'phone_number': None},
        {'full_name': contact_info['full_name'], 'email': None, 'phone_number': contact_info['phone_number']},
        {'full_name': None, 'email': contact_info['email'], 'phone_number': contact_info['phone_number']},
        {'full_name': contact_info['full_name'], 'email': contact_info['email'],
         'phone_number': contact_info['phone_number']}
    ]

    return scenarios[scenario_num]


def evaluate_contact_information(scenario_num):
    global total_tests, successful_tests
    total_tests += 1

    ask_information = [
        HumanMessage(content="I want to talk to a human representative."),
        AIMessage(
            content="I'm sorry, but I need your full name, email, and phone number to connect you with a human representative. Can you please provide that information?")
    ]

    contact_information_generated = generate_random_contact_info(scenario_num)
    full_name = contact_information_generated.get('full_name')
    email = contact_information_generated.get('email')
    phone_number = contact_information_generated.get('phone_number')

    provided_info = ", ".join(filter(None, [full_name, email, phone_number]))
    contact_information_question = {"user_input": provided_info}

    response = chatbot.chatbot_response(contact_information_question["user_input"], evaluate_mode=True,
                                        mess=ask_information)

    if scenario_num == 6:
        # I DID NOT FIND A WAY TO TEST THE SCENARIO  WHERE THE CONTACT INFORMATION ALREADY EXISTS IN OUR RECORDS
        # contact_information_question['expected_response'] = "Contact information already exists in our records. Is there anything else I can do ?"
        contact_information_question[
            'expected_response'] = "Contact information saved successfully. Is there anything else i can do ?"
    else:
        contact_information_question[
            'expected_response'] = "I'm sorry, but I need your full name, email, and phone number to connect you with a human representative. Can you please provide that information?"

    print(f"User: I want to talk to a human representative.")
    print(
        f"Bot: I'm sorry, but I need your full name, email, and phone number to connect you with a human representative. Can you please provide that information?")
    print(f"User: {contact_information_question['user_input']}")
    print(f"Bot: {response}")
    print(f"Expected: {contact_information_question['expected_response']}")
    print(f"Match: {contact_information_question['expected_response'] in response}\n")
    if contact_information_question['expected_response'] in response:
        successful_tests += 1



if __name__ == "__main__":
    for i in range(7):
        chatbot.initialize_chatbot()
        evaluate_status_order()
        create_status_id_questions()
        evaluate_request_human_representative()
        evaluate_contact_information()
        evaluate_return_policy()
        evaluate_non_returnable_items()
        evaluate_refund_process()

    # Calculate and print accuracy
    accuracy = successful_tests / total_tests * 100
    print(f"Accuracy: {accuracy:.2f}%")
