import streamlit as st
import numpy as np
import pandas as pd
import openai
import time
from tqdm import tqdm

# Importing helper classes from external modules
from gpt_index import SimpleDirectoryReader, GPTListIndex, GPTTreeIndex, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain import OpenAI

import sys
import os
import pandas as pd
import warnings

# Set OpenAI API key as an environment variable
os.environ["OPENAI_API_KEY"] = "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"  # Replace 'xxx' with your API key

def ask_bot(q, input_index='index.json'):
    """
    Function to generate a response for the user query using OpenAI's GPT-3 language model.
    
    Parameters:
    q (str): The user query for which a response is to be generated.
    input_index (str): The path to the index file to be used for querying the language model.
                       The default value is 'index.json'.
    
    Returns:
    str: The response generated by the language model for the given user query.
    """
    index = GPTSimpleVectorIndex.load_from_disk(input_index)
    exit = True
    while exit:
        query = q
        if query == 'exit':
            exit = False
            continue
        response = index.query(q, response_mode="compact")
        print("\nBot says: \n\n" + response.response + "\n\n\n")
        return response.response 

def get_bot_response(message):
    """
    Function to get the chatbot response for a user message.
    
    Parameters:
    message (str): The user message for which a response is to be generated.
    
    Returns:
    str: The chatbot response generated by the ask_bot function.
    """
    return ask_bot(message, 'review.json')

def chatbot():
    """
    Function to create the Streamlit UI for the chatbot and handle user interactions.
    """
    st.title("Chatbot with Streamlit and ChatterBot")
    user_input = st.text_area("You", "", height=100)
    chat_history = st.empty()
    if st.button("Send"):
        response = get_bot_response(user_input)
        chat_history.write("You: " + user_input)
        chat_history.write("Bot: " + response)
        user_input = ""

if __name__ == '__main__':
    chatbot()

