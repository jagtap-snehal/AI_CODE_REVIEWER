from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st
import google.generativeai as genai

# Configure the GenAI API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the generative model
model = genai.GenerativeModel("gemini-1.5-flash")

# Define the system prompt for the AI reviewer
sys_prompt = """
You are a highly skilled AI code reviewer built into an intuitive Python application. Your task is to analyze Python scripts submitted by users and provide:
1. ## Bug Report: Highlight any issues such as potential bugs, syntax errors, or logical mistakes.
2. ## Fixed Code: Share corrected or optimized versions of the submitted code, including detailed explanations of the improvements made.
3. ## User Assistance: Deliver feedback that is straightforward, professional, and tailored for developers of different experience levels.
Ensure feedback is clear, actionable, and focuses on best practices to enhance code quality and user learning.
"""


def get_response(system_prompt, user_code):
    response = model.generate_content([system_prompt, user_code])
    return response.text


st.title(":robot_face: AI-Powered Code Reviewer")


code_input = st.text_area("Paste your Python code here:")


generate_button = st.button("Review Code")

st.header("Review Results")


if generate_button:
    try:
        result = get_response(sys_prompt, code_input)
        st.write(result)
    except Exception as error:
        st.error(f"An error occurred: {error}")