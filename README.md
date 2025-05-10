# 🤖 Customer Support Chatbot

A simple yet effective command-line-based customer support chatbot built using **Python**, **scikit-learn**, and **Multinomial Naive Bayes**. It helps classify user queries into predefined categories like password reset, order status, and more.

## 📌 Features

- Classifies user queries into categories like:
  - Password Reset
  - Order Status
  - Product Return
  - Package Tracking
  - Discounts
  - Contact Support
  - Shipping Address
  - Order Cancellation
- Real-time interaction via command-line interface
- Machine learning model using `MultinomialNB` and `CountVectorizer`
- Lightweight and easy to extend

---

## 🧠 Technologies Used

- **Python 3.x**
- **scikit-learn**
- **pandas**
- **numpy**
- **matplotlib** (optional, currently unused)
- **Multinomial Naive Bayes**
- **CountVectorizer**

---

## 🗂️ Project Structure
- **customer-support-chatbot/**
- **│**
- **├── chatbot.py # Main chatbot script**
- **├── README.md # Project documentation**
- **├── requirements.txt # Required Python packages**
- **└── dataset.csv (optional if loading from CSV)**

---

## 📌 How It Works
- Uses CountVectorizer to convert text queries into numerical vectors.

- Trains a MultinomialNB model on labeled support queries.

- Accepts user input via the terminal.

- Predicts the category of the query and responds with an appropriate support topic.

- User can type exit to quit the chatbot.

## 🔮 Future Enhancements
- Expand dataset with more real-world queries

- Add confidence scores to predictions

- Integrate with a web-based or mobile UI

- Support for multi-language input

- Upgrade model to transformer-based NLP (e.g., BERT or GPT)

   
## 📁 Dataset

The sample dataset is hardcoded for simplicity and contains frequently asked support questions with corresponding categories:

```python
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





