# process_requests.py

import re
import sqlite3
import csv
import os

def extract_number(answer):
    number_match = re.search(r'(\d+)', answer)
    if number_match:
        return int(number_match.group(1))
    else:
        return None


def extract_order_id(answer):
    order_id_match = re.search(r'The order ID is: "?(\w+)"?', answer)
    if order_id_match:
        order_id = order_id_match.group(1)
        return order_id
    else:
        return None


def fetch_order_status(order_id):
    conn = sqlite3.connect('ecommerce.db')
    c = conn.cursor()
    c.execute('SELECT status FROM Orders WHERE order_id = ?', (order_id,))
    order = c.fetchone()
    if order:
        order_status = order[0]
        return f"For your order ID {order_id}, the status is {order_status}.\nIs there anything else I can do ?"
    else:
        return f"Your order ID {order_id} was not found, it might be misspelled so please check the order ID and try again."


def process_contact_information(user_input):
    # Adjust the regex pattern to capture the contact information correctly
    contact_info_pattern = re.compile(r"Name:\s*([^,]+),\s*Email:\s*([^,]+),\s*Phone:\s*(\d+)")
    match = contact_info_pattern.search(user_input)

    if match:
        name, email, phone = match.groups()
        filename = f"{email}_contact_info.csv"

        if os.path.exists(filename):
            return "Contact information already exists in our records. Is there anything else I can do ?"

        else:
            with open(filename, mode="a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([name, email, phone])
            return "Contact information saved successfully. Is there anything else i can do ?"
    else:
        return "I'm sorry, but I need your full name, email, and phone number to connect you with a human representative. Can you please provide that information?"

