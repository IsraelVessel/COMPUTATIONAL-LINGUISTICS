import gradio as gr
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training data
training_sentences = [
    "hello", "hi", "good morning",
    "bye", "goodbye", "see you later",
    "how are you", "what's up", "how is it going",
    "thanks", "thank you"
]

training_labels = [
    "greeting", "greeting", "greeting",
    "farewell", "farewell", "farewell",
    "how_are_you", "how_are_you", "how_are_you",
    "thanks", "thanks"
]

# Vectorize text
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(training_sentences)

# Train Naive Bayes classifier
clf = MultinomialNB()
clf.fit(X_train, training_labels)

# Response dictionary
responses = {
    "greeting": "Hello there! 😊",
    "farewell": "See you soon! 👋",
    "how_are_you": "I'm just code, but I'm doing fine. How about you?",
    "thanks": "You're welcome! 🙌"
}

# Chat function
def chatbot_response(user_input):
    X_test = vectorizer.transform([user_input])
    prediction = clf.predict(X_test)[0]
    return responses.get(prediction, "Sorry, I don't understand that.")

# Gradio Interface
demo = gr.Interface(
    fn=chatbot_response,
    inputs=gr.Textbox(lines=2, placeholder="Type your message here..."),
    outputs="text",
    title="Simple AI Chatbot",
    description="A basic AI chatbot built with Python, scikit-learn, and Gradio."
)

if __name__ == "__main__":
    demo.launch()
    share=True  