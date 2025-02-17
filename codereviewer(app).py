import streamlit as st
import google.generativeai as genai

# Read API key and initialize Gemini client
with open("keys/Gemini.txt") as f:
    key = f.read().strip()
genai.configure(api_key=key)

# Custom Page Layout
st.set_page_config(page_title="AI Code Reviewer", layout="centered")

# Title with Icon
st.markdown("<h1 style='text-align: center;'>🔍 AI Code Reviewer (Gemini)</h1>", unsafe_allow_html=True)
st.markdown("## 📌 Enter your Python code below for AI-powered review!")

# Text area for user to input Python code
code_input = st.text_area("📝 Code Editor", height=300, placeholder="Write or paste your Python code here...")

# Custom Styling for Button
st.markdown(
    """<style>
    div.stButton > button:first-child {
        background-color: #FF4B4B;
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 8px;
        width: 100%;
    }
    </style>""",
    unsafe_allow_html=True
)

# Review Code Button
if st.button("🚀 Review Code"):
    if code_input.strip() == "":
        st.warning("⚠️ Please enter some Python code for review.")
    else:
        # Gemini Prompt for Code Review
        prompt = f"""
        You are an expert Python code reviewer. Analyze the following Python code for errors, bugs, and improvements.
        Provide a structured bug report and suggest a corrected version of the code.

        Python Code:
        ```
        {code_input}
        ```

        Return the response in the following format:

        **Bug Report:**
        - List of identified issues.

        **Fixed Code:**
        ```python
        # Corrected version of the code
        ```
        """

        # Request response from Gemini API
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)

        # Display AI-generated bug report and fixed code
        st.markdown("### 🐞 Bug Report & Fixes")
        st.code(response.text, language="markdown")
