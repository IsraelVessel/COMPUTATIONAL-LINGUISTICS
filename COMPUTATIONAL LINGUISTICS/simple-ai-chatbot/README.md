# Simple AI Chatbot

This project is a simple AI chatbot built using Python, Gradio, and scikit-learn. The chatbot is designed to respond to user inputs with predefined responses based on the type of message received.

## Project Structure

```
simple-ai-chatbot
├── src
│   └── app.py          # Main code for the AI chatbot
├── requirements.txt    # Dependencies required for the project
└── README.md           # Documentation for the project
```

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd simple-ai-chatbot
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Chatbot

To run the chatbot, execute the following command:

```
python src/app.py
```

This will launch a Gradio interface in your web browser where you can interact with the chatbot.

## Functionality

The chatbot can respond to the following types of messages:

- Greetings (e.g., "hello", "hi")
- Farewells (e.g., "bye", "goodbye")
- Inquiries about well-being (e.g., "how are you", "what's up")
- Expressions of gratitude (e.g., "thanks", "thank you")

## Hosting

You can host the chatbot on platforms such as:

- **Heroku**: A cloud platform that supports Python applications and can easily deploy Gradio interfaces.
- **Google Cloud Platform**: Offers various services to host and run your applications.
- **Streamlit Sharing**: A platform specifically designed for sharing Streamlit apps, which can also support Gradio interfaces.

Feel free to explore these options to make your chatbot accessible to users online!