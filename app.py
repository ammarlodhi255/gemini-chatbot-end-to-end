import streamlit as st
from model import get_model

model = get_model()
chat = model.start_chat(history=[])

def get_response(question):
    response = chat.send_message(question, stream=True)
    return response 

# Initialize streamlit
st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Conversation Application")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

if submit and input:
    response = get_response(input)
    # Add to chat history
    st.session_state['chat_history'].append(("You:", input))
    st.subheader("The response is")

    # Show messages in chunks rather than waiting for the entire response.
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot:", chunk.text))

st.subheader("The chat history is")

for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")