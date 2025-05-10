import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


data = {
    'question': [
        "How can I reset my password?", 
        "I want to check my order status", 
        "How to return a product?", 
        "Where is my package?", 
        "Do you offer discounts?", 
        "How can I contact support?", 
        "Can I change my shipping address?", 
        "Can I cancel my order?"
    ],
    'category': [
        "Password Reset", 
        "Order Status", 
        "Product Return", 
        "Package Tracking", 
        "Discounts", 
        "Contact Support", 
        "Shipping Address",   
        "Order Cancellation"
    ]
}

df = pd.DataFrame(data)


X = df['question']
y = df['category']


model = make_pipeline(CountVectorizer(), MultinomialNB())


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)


def chatbot_response(query):
    prediction = model.predict([query])
    return prediction[0]


print("Hello! I'm your customer support chatbot.")
print("How can I Help You?")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Goodbye! Have a great day.")
        break
    response = chatbot_response(user_input)
    print(f"Bot: I can help with {response}")


accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy * 100:.2f}%")
