<h1 align=center>
  Gemini Workshop
</h1>

This workshop featured an email generator project which uses Gemini AI to write emails easily.

## 🚀 Quick start
<!-- Write the dependencies -->
1. **Install the dependencies**
```sh
pip install streamlit google-generativeai
```

2. **Get your API key**
<!-- API key from URL -->
    Get your API key from [Gemini AI](https://makersuite.google.com/app/apikey)

3. **Run the app**
```sh
streamlit run app.py
```

## 📝 Usage
<!-- How to use the app -->
1. **Write who the email is for**
2. **Write who the email is from**
3. **Write the subject of the email**
4. **Write what the email is about i.e. give context to Gemini**
5. **Click on the generate button**

## 📸 Screenshots
![image](https://github.com/GDSC-VESIT/gemini_workshop/assets/142719235/a152cbbf-e853-46f4-aa7c-1f0a6d5b3fd0)
![image](https://github.com/GDSC-VESIT/gemini_workshop/assets/142719235/348e9b23-a9e3-4b10-9a73-89246203ac22)
![image](https://github.com/GDSC-VESIT/gemini_workshop/assets/142719235/ac766112-d121-48ac-872f-4bde507c3f7c)


## 🔗 Deployment steps
<!-- How to deploy the app -->
1. **Create account on Streamlit sharing**
2. **Create a new app**
3. **Connect your GitHub repository**
4. **Save your API key as a secret in Streamlit**
    - Make changes in your code
    - Change the line of API key to the line as follows
    ```python
    api_key = st.secrets["api_key"]
    ```
5. **Click on deploy**
