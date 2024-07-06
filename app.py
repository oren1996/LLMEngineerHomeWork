import os
from flask import Flask, render_template, request, jsonify
from chatbot import initialize_chatbot, chatbot_response
from create_database import initialize_database
from create_data import add_data

app = Flask(__name__)

# Initialize the chatbot
initialize_chatbot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']
    response_message = chatbot_response(user_message)
    return jsonify({'response': response_message})

@app.route('/initialize_bot', methods=['POST'])
def initialize_bot():
    initialize_chatbot()
    return jsonify({'message': 'Bot initialized with welcome message'})

if __name__ == '__main__':
    app.run(debug=True)
