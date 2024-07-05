import streamlit as st
from chatbot import chatbot_response, welcome_message, initialize_chatbot, main


# Streamlit UI setup
st.set_page_config(page_title="Customer Support Chatbot", page_icon=":robot_face:")
st.markdown("<h1 style='text-align: center;'>Customer Support Chatbot</h1>", unsafe_allow_html=True)

# Initialize session state variables
if 'messages' not in st.session_state:
    st.session_state['messages'] = []
    initialize_chatbot()
    # main()
    st.session_state['messages'].append({"role": "assistant", "content": welcome_message})

st.sidebar.title("Sidebar")
clear_button = st.sidebar.button("Clear Conversation", key="clear")

# Reset conversation
if clear_button:
    st.session_state['messages'] = []
    initialize_chatbot()
    st.session_state['messages'].append({"role": "assistant", "content": welcome_message})

# Display previous messages
for message in st.session_state['messages']:
    role = message["role"]
    content = message["content"]
    with st.chat_message(role):
        st.markdown(content)

# Chat input
prompt = st.chat_input("You:")
if prompt:
    st.session_state['messages'].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = chatbot_response(prompt)
    st.session_state['messages'].append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
