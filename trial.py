import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")
prompt = "Tell me about India"
response = model.generate_content(prompt)
print(response.text)