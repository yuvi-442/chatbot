                                                             Revolutionizing customer support with an intelligent chatbot for automated assistance.

📖 Project Overview

            This project is a simple customer support chatbot built using Python, leveraging the Multinomial Naive Bayes classification model and the CountVectorizer from scikit-learn. The chatbot takes user queries as input and classifies them into predefined categories such as password reset, order status, or contact support.

            The aim is to simulate a lightweight FAQ chatbot that can assist users with their questions in real time using basic natural language processing and supervised machine learning.

❓ Problem Statement
         Many e-commerce websites and service platforms face high volumes of repetitive customer queries. Answering frequently asked questions (FAQs) like "How to reset my password?" or "Where is my package?" consumes valuable customer service resources.

        The goal of this chatbot is to automate the first level of customer interaction by identifying the intent of a user's question and routing it to the appropriate category or providing a predefined response. This reduces customer service workload and enhances response speed and user satisfaction.

🎯 Objectives
     Build a chatbot to classify customer queries into relevant categories.

     Use text classification with CountVectorizer and Multinomial Naive Bayes.

    Develop a minimal interactive console-based chatbot.

    Train and test the model using a small set of labeled examples.

    Evaluate model performance using accuracy metrics.

    Offer a foundation for scaling into more advanced chatbot systems.
 
🛠 Technology Stack
Programming Language: Python 3.x

Libraries Used:

          scikit-learn: For vectorization and classification.

          pandas and numpy: For data handling.

          matplotlib: (Optional) for visualizing accuracy or model insights.

          Machine Learning Algorithm: Multinomial Naive Bayes

          Vectorizer: CountVectorizer (Bag-of-Words model)

📊 Dataset Description
          This chatbot uses a very small hardcoded dataset containing eight common user questions and their corresponding categories. Each entry includes:

Question	Category
         How can I reset my password?	Password Reset
         I want to check my order status	Order Status
         How to return a product?	Product Return
         Where is my package?	Package Tracking
         Do you offer discounts?	Discounts
         How can I contact support?	Contact Support
         Can I change my shipping address?	Shipping Address
         Can I cancel my order?	Order Cancellation

This small dataset is used to simulate intent classification for a customer support chatbot.

🧠 Model Architecture
        The chatbot is powered by a text classification pipeline:

        CountVectorizer: Converts input text into a matrix of token counts.

        Multinomial Naive Bayes: Trained on tokenized data to classify the intent.

Pipeline Structure:

      graphql:

            Input Query → CountVectorizer → MultinomialNB → Category Output
            The model learns word-frequency patterns associated with each support category and uses probabilistic reasoning to predict the closest category for new queries.

⚙️ Working Mechanism
            User types a question into the console.

            The chatbot processes the input using the vectorizer.

            The trained Naive Bayes model predicts the most likely category.

            The chatbot responds with the related support area.

📜 Code Explanation
       python code:

          import numpy as np
          import pandas as pd
          from sklearn.feature_extraction.text import CountVectorizer
          from sklearn.naive_bayes import MultinomialNB
          from sklearn.pipeline import make_pipeline
          from sklearn.model_selection import train_test_split
          import matplotlib.pyplot as plt
          
Libraries for data manipulation, machine learning, and visualization.
 
pythoncode:

data = {
    'question': [
        "How can I reset my password?",
        "I want to check my order status",
        ...
    ],
    'category': [
        "Password Reset",
        "Order Status",
        ...
    ]
}
  
df = pd.DataFrame(data)
Dataset stored as a dictionary and converted into a DataFrame.

python code:

X = df['question']
y = df['category']
X: Input questions.

y: Target labels (categories).

python code:

model = make_pipeline(CountVectorizer(), MultinomialNB())
Creates a processing pipeline for vectorization and classification.

python
Copy
Edit
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)
Data is split into training and test sets (80/20) and the model is trained.

           python code:

def chatbot_response(query):
    prediction = model.predict([query])
    return prediction[0]
Predicts category for a user input.

           python code:

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Goodbye! Have a great day.")
        break
    response = chatbot_response(user_input)
    print(f"Bot: I can help with {response}")
Runs a loop to simulate an ongoing chatbot interaction.

            python code:

       accuracy = model.score(X_test, y_test)
       print(f"Model Accuracy: {accuracy * 100:.2f}%")
       Outputs model performance.

💻 Installation Guide
Clone the Repository (if applicable):


git clone https://github.com/yourusername/chatbot.git
cd chatbot
Install Required Libraries:


pip install numpy pandas scikit-learn matplotlib
Run the Script:


python chatbot.py
▶️ How to Run
Once you execute the script, you will see:


  Hello! I'm your customer support chatbot.
  How can I Help You?
  You: 
Start typing your query, e.g.:
 
You: I forgot my password
Bot: I can help with Password Reset
Type exit to terminate the chatbot.

🧪 Testing and Accuracy
   The model is evaluated using a simple accuracy score:

python code:

  model.score(X_test, y_test)
  With 8 examples, the split gives only 1–2 test samples. Accuracy may vary significantly and isn't statistically significant due to the tiny dataset.

Example Output:

  Model Accuracy: 100.00%

📥 Sample Inputs and Outputs
User Input	Predicted Category
   “Where is my order?”	Package Tracking
   “I want to return this item”	Product Return
   “How do I get in touch?”	Contact Support
   “Do you give any coupon?”	Discounts
   “Cancel the order I made today”	Order Cancellation

🔧 Improvements and Future Scope
   Expand dataset to hundreds or thousands of diverse queries.

   Add synonyms and paraphrasing to improve intent recognition.

   Integrate Named Entity Recognition (NER) for more personalized responses.

   Move from console to GUI or web-based interface using Flask/Django.

   Incorporate a dialogue history for better context awareness.

Add multilingual support.

Use more advanced models like BERT or GPT for dynamic conversations.

⚠️ Limitations
   Small dataset results in overfitting and lack of generalization.

   Fails on queries not similar to the trained samples.

   No real-time backend integration or database support.

   Only supports hardcoded questions and categories.

   Not context-aware; each query is treated independently.

✅ Conclusion
                This project serves as a foundational prototype of a machine learning-based customer support chatbot using Python and scikit-learn. While limited in scope, it effectively demonstrates 
                the power of natural language processing combined with classic machine learning to classify user queries and simulate a conversational agent. With further development, this system can 
                be scaled into a production-grade smart assistant.

📚 References
          scikit-learn Documentation

          Python Official Docs

          CountVectorizer

          MultinomialNB

          Naive Bayes Text Classification

[Customer Support Bots - IBM, AWS Examples]

Team Members and Roles
  ●	Yuvaraj.k: Introduction,Documentation and final report.
  ●	Suman.R: Model development and testing.
  ●	Saravanan.v: Visualization and deployment.
  ●	Pravin kumar.M: Data collection and cleaning.


