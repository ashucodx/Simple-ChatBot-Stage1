# Simple Chatbot

This is a simple rule-based chatbot created using Python and the NLTK library. The chatbot can respond to basic greetings and questions.

## Features

- Responds to basic greetings like "hi", "hello", "hey".
- Provides information about the chatbot.
- Can handle simple questions and provides fallback responses for unrecognized input.

## Requirements

- Python 3.x
- NLTK library

## Installation

1. **Clone the Repository**:

    ```sh
    git clone https://github.com/ashucodx/Simple-ChatBot-Stage1.git
    cd simple-chatbot
    ```

2. **Install Dependencies**:

    Make sure you have `pip` installed. Then, install the required libraries:

    ```sh
    pip3 install nltk
    ```

3. **Download NLTK Data**:

    Open a Python shell and download the necessary NLTK data:

    ```python
    import nltk
    nltk.download('punkt')
    ```

## Usage

Run the chatbot using the following command:

```sh
python3 chatbot.py

Interact with the Chatbot
The chatbot will start and you can interact with it by typing in the terminal. Type 'quit' to exit the chatbot.

Example
```sh
Here is an example interaction with the chatbot:
Hi! I am a simple chatbot. Type 'quit' to exit.
You: hi
Chatbot: Hello!
You: what is your name ?
Chatbot: My name is Chatbot. I am a chatbot created by you.
You: how are you ?
Chatbot: I am fine, thank you.
You: quit
Chatbot: Bye! Take care.
```
Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

Acknowledgements
NLTK - Natural Language Toolkit library
