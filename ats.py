# import libraries
import streamlit as st
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import google.generativeai as genai

# Load env variable
load_dotenv()  

# Initialize the API with your API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load prompt from file
def load_prompt(role):
    prompt_folder = "prompts"
    prompt_file = os.path.join(prompt_folder, f"{role}.txt")
    with open(prompt_file, "r") as f:
        prompt = f.read()
    return prompt

# Function to extract text from uploaded PDF
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += str(page.extract_text())
    return text

# Function to get response from generative model
def get_response(input_prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input_prompt)
    return response.text

# Streamlit app
st.set_page_config(layout="wide")
st.title("ATS Results")
st.markdown("---")

# Sidebar
st.sidebar.title("Upload Files")
role = st.sidebar.text_input("Enter Job/Role Title")
jd = st.sidebar.text_area("Enter the Job Description")
advanced_criteria = st.sidebar.text_area("Advanced Criteria (Optional)", help="Enter any additional instructions or criteria you want to consider for matching.")
uploaded_file = st.sidebar.file_uploader("Upload your Resume", type="pdf", help="Please Upload the PDF")
submit = st.sidebar.button("Submit")

if submit:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        input_prompt = load_prompt(role).format(text=text, jd=jd, advanced_criteria=advanced_criteria)
        
        # Use the input prompt with the generative AI API
        response = get_response(input_prompt)
        
        # Extracting profile match percentage, missing keywords, highlighted keywords, removable keywords, and experience relevance from the response
        response_parts = response.split('"')
        if len(response_parts) >= 6:
            match_percentage = response_parts[3]
            missing_keywords_section = response_parts[7] if len(response_parts) > 7 else ""
            highlighted_keywords_section = response_parts[11] if len(response_parts) > 11 else ""
            removable_keywords_section = response_parts[15] if len(response_parts) > 15 else ""
            experience_relevance = response_parts[19] if len(response_parts) > 19 else ""
            
            st.subheader(f"Profile Match: {match_percentage}")
            st.subheader(f"Missing Keywords: {missing_keywords_section}")
            st.subheader(f"Highlighted Keywords: {highlighted_keywords_section}")
            st.subheader(f"Removable Keywords: {removable_keywords_section}")
            #st.subheader("Experience Relevance:")
            #st.write(experience_relevance)
        else:
            st.write("Response format is not as expected.")
