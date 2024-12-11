
# import streamlit as st
# import pickle
# import random
# import sys
# import os

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from bot.preprocess import preprocess_text
# from bot.preprocess import load_intents

# # Load the model and vectorizer
# with open("bot/model.pkl", "rb") as model_file:
#     model = pickle.load(model_file)

# with open("bot/vectorizer.pkl", "rb") as vectorizer_file:
#     vectorizer = pickle.load(vectorizer_file)

# # Load intents
# intents = load_intents("bot/intents.json")

# # Mapping intent labels
# label_map = {intent["tag"]: idx for idx, intent in enumerate(intents["intents"])}

# # Function to get chatbot response
# def get_response(user_input):
#     # Preprocess the user input
#     user_input = preprocess_text(user_input)
#     input_vector = vectorizer.transform([user_input])
#     prediction = model.predict(input_vector)[0]
#     intent = list(label_map.keys())[prediction]

#     # Initialize the response variable
#     response = "Here are a few ideas which you can implement:\n\n"
    
#     # Check if the query matches any tag (AI, ML, etc.)
#     for intent_data in intents["intents"]:
#         if intent_data["tag"] == intent:
#             response += "\n".join(intent_data["responses"]) + "\n"
#             break
#     return response

# # Streamlit UI
# def main():
#     st.title("Project Guide Chatbot")
#     st.write("Ask me about project ideas or innovations in domains like AI, ML, Blockchain, IoT, etc.")

#     #user_input = st.text_input("Enter a domain or topic:", "")
#     user_input = st.text_area("Enter a domain or topic:", height=150)
    
#     if st.button("Get Project Ideas"):
#         if user_input.strip():
#             response = get_response(user_input)
#             st.write(f"Guide: {response}")
#         else:
#             st.write("Please enter a valid domain or topic to get project ideas.")

# if __name__ == "__main__":
#     main()
import streamlit as st
import pickle
import random
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bot.preprocess import preprocess_text
from bot.preprocess import load_intents

# Load the model and vectorizer
with open("bot/model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("bot/vectorizer.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Load intents
intents = load_intents("bot/intents.json")

# Mapping intent labels
label_map = {intent["tag"]: idx for idx, intent in enumerate(intents["intents"])}

# Function to get chatbot response
def get_response(user_input):
    # Preprocess the user input
    user_input = preprocess_text(user_input)
    input_vector = vectorizer.transform([user_input])
    prediction = model.predict(input_vector)[0]
    intent = list(label_map.keys())[prediction]

    # Initialize the response variable
    response = "Here are a few ideas which you can implement:\n\n"
    
    # Check if the query matches any tag (AI, ML, etc.)
    for intent_data in intents["intents"]:
        if intent_data["tag"] == intent:
            response += "\n".join(intent_data["responses"]) + "\n"
            break
    return response

# Streamlit UI
def main():
    # Custom CSS for better styling and animations
    st.markdown(
        """
        <style>
            body {
                background-color: #f1f8ff;
                font-family: 'Arial', sans-serif;
                color: #333;
                margin: 0;
                padding: 0;
            }
            h1 {
                color: #ffffff;
                font-size: 36px;
                text-align: center;
                font-weight: bold;
                margin-top: 10px;
                background-color: #B1F0F7;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                animation: fadeIn 1s ease-out;
            }
            .card {
                background-color:#C6E7FF;
                padding: 20px;
                font-size: 26px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                margin: 20px 0;
                animation: fadeIn 1s ease-out;
            }
            .input-card {
                background-color: #e3f2fd;
                padding: 20px;
                border-radius: 10px;
                width: 60%;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                margin: auto;
                animation: fadeIn 1s ease-out;
            }
            .stTextInput>div>div>input {
                font-size: 18px;
                padding: 12px 20px;
                border-radius: 10px;
                width: 100%;
            }
            .stButton {
                background-color: transparent;
                color: #008CBA;
                padding: 10px 20px;
                border-radius: 10px;
                font-size: 18px;
                margin-top: 20px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                width: 100px;
                margin-left: auto;
                margin-right: auto;
                display: block;
            }
            .stButton:hover {
                background-color: #C6E7FF;
                cursor: pointer;
                color:#008CBA;
            }
            .response-card {
                font-size: 22px;
                line-height: 1.6;
                background-color: #e3f2fd;
                color: #004e92;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
                margin-top: 20px;
                animation: fadeIn 1s ease-out;
            }
            @keyframes fadeIn {
                0% { opacity: 0; transform: translateY(-30px); }
                100% { opacity: 1; transform: translateY(0); }
            }
            .stWrite {
                text-align: center;
                font-size: 18px;
                margin-top: 20px;
            }
            .stContainer {
                display: flex;
                justify-content: center;
                align-items: center;
                flex-direction: column;
            }
        </style>
        """, unsafe_allow_html=True
    )

    st.markdown('<h1>✨ Project Ideas Chatbot ✨</h1>', unsafe_allow_html=True)

    # Display introductory message in card layout
    st.markdown('<div class="card">Ask me about project ideas or innovations ...!</div>', unsafe_allow_html=True)

    # Input card with a large text area
    with st.container():
        #st.markdown('<div class="input-card">', unsafe_allow_html=True)
        user_input = st.text_area("Enter a domain or topic:", height=70, max_chars=100, key="input_field", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

    # Loading spinner while processing the input
    with st.spinner("Thinking..."):
        if st.button("Get Project Ideas", key="get_ideas_button"):
            if user_input.strip():
                response = get_response(user_input)
                # Response card with animation
                st.markdown(f'<div class="response-card">{response}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="response-card">Please enter a valid domain or topic to get project ideas.</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
