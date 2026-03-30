MindScope: Overthinking Detection using AI

 Overview:

MindScope is a simple AI-based project that analyzes user input text and detects whether it reflects overthinking behavior or normal thinking patterns.

Unlike basic sentiment analysis (positive/negative), this project focuses on identifying cognitive patterns such as:

Repetitive thoughts
Excessive worrying (“what if” thinking)
Negative looping

The goal is to create a small but meaningful system that can understand thought patterns, not just emotions.

 Features:
Detects overthinking from text input
Provides instant prediction
Displays result in a simple web interface
Beginner-friendly implementation using Machine Learning
Lightweight and fast

Technologies Used:
Python → core programming
pandas → data handling
scikit-learn → machine learning model
TF-IDF Vectorizer → text to numerical conversion
Logistic Regression → classification model
Streamlit → web application interface

How It Works:
A small dataset of sentences is created manually.
Each sentence is labeled as:
1 → Overthinking
0 → Normal
The text data is converted into numerical form using TF-IDF.
A Logistic Regression model is trained on this data.
The trained model is saved using pickle.
A Streamlit app is used to:
Take user input
Process it
Predict the result in real-time

Project Structure:
OverthinkingAI/
│── data.csv           # Dataset
│── model.py           # Model training script
│── app.py             # Streamlit app
│── model.pkl          # Saved trained model
│── vectorizer.pkl     # Saved TF-IDF vectorizer
│── README.md          # Project documentation


Installation & Setup:
1. Clone or download the project
2. Install dependencies
pip install pandas scikit-learn streamlit
3. Train the model
python model.py
4. Run the application
streamlit run app.py

 Example Input:

Input:

What if I fail again and everything goes wrong?

Output:

Overthinking detected

Learning Outcomes

Through this project, I learned:

Basics of Natural Language Processing (NLP)
How to convert text into numerical features
Training and saving ML models
Building simple web apps using Streamlit
End-to-end ML workflow (data → model → UI)

Disclaimer:

This project is for educational purposes only and should not be used as a medical or psychological diagnosis tool.

Author:

Developed by Ansh Jain
