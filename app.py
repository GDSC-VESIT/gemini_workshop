import google.generativeai as genai
import streamlit as st
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

def get_email(src, dest, subject, tone, about):
    prompt = "Write an email from {} to {}. Subject line is {}. Keep the email {}.The email is regarding {}.".format(src, dest, subject, tone, about)
    response = model.generate_content(prompt)
    return response.text

# prepare empty web page
st.set_page_config(
    page_title = "Email generator",
    page_icon = ":email:",
    layout = "centered",
    initial_sidebar_state = "collapsed"
)

st.header("Write emails like a professional")
st.write("Desribe the type of email you want. Gemini will write it for you.")

col1, col2 = st.columns(2)

with col1:
    src = st.text_input("Who is this email from? E.g. student")
    subject = st.text_input("Subject")

with col2:
    dest = st.text_input("Who is this email for? E.g. HOD")
    tone = st.selectbox("Choose the tone of your email", ["Formal", "Informal", "Casual", "Funny", "Angry"])

about = st.text_area("What is the email about?")

send_request = st.button("Generate email")

if send_request:
    if src and subject and dest and tone and about:
        st.write(get_email(src, dest, subject, tone, about))
    else:
        st.error("Please fill all the fields.")