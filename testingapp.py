import streamlit as st
import google.generativeai as genai
st.title("MY AI APP")
genai.configure(api_key="AIzaSyBcwMbtKtUFjGoXagqdeIOmZ-iO4t4sq30")
text = st.text_input("Enter a Question:")
if st.button("Clike Me"):
    if text.strip():
        model = genai.GenerativeModel('gemini-pro')
        chat = model.start_chat(history=[])
        response = chat.send_message(text)
        st.html("<p><Strong> Answer for above question<Strong></p>")
        st.write(response.text)
    else:
        st.info("Please enter a question")
    
