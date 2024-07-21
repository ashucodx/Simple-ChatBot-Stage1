import nltk
from nltk.chat.util import Chat, reflections
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey!"]
    ],
    [
        r"what is your name ?",
        ["My name is Chatbot.", "I am a chatbot created by you."]
    ],
    [
        r"how are you ?",
        ["I am fine, thank you.", "I am doing well!"]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye!"]
    ],
    [
        r"what is your favorite color ?",
        ["I don't have a favorite color.", "I am just a bunch of code!"]
    ],
    [
        r"what is the weather like ?",
        ["I don't know the weather, but you can check online."]
    ],
]
chatbot = Chat(pairs, reflections)
def start_chatbot():
    print("Hi! I am a simple chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: Bye! Take care.")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    start_chatbot()

def fallback_response():
    return "I don't understand that."

class SimpleChat(Chat):
    def respond(self, statement):
        response = super().respond(statement)
        return response if response else fallback_response()

chatbot = SimpleChat(pairs, reflections)
