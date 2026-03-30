import streamlit as st
import pickle

st.set_page_config(page_title="MindScope AI", layout="centered")
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("🧠 MindScope - Overthinking Detector")

st.write("Enter your thoughts and let AI analyze your thinking pattern.")

user_input = st.text_area("Type here:")

if st.button("Analyze"):

    if user_input.strip() != "":
        
        input_vector = vectorizer.transform([user_input])
        
        prediction = model.predict(input_vector)[0]
        

        probability = model.predict_proba(input_vector)[0][1]


        if prediction == 1:
            st.error("⚠️ Overthinking Detected")
            st.write(f"Confidence: {probability:.2f}")
            st.info("Suggestion: Take a break, write your thoughts down, or distract your mind.")
        else:
            st.success("✅ Balanced Thinking")
            st.write(f"Confidence: {1 - probability:.2f}")

    else:
        st.warning("Please enter some text.")