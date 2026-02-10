import nltk
from nltk.chat.util import Chat, reflections
# Sample training data
pairs = [
    ['hi', ['Hello!', 'Hi there!', 'How can I help you?']],
    ['hello', ['Hello!', 'Hi there!', 'How can I help you?']],
    ['how are you', ['I am doing well, thank you!', 'I\'m good, thanks for asking.']],
    ['what is your name', ['My name is Chatbot.', 'I am a chatbot.']],
    # Add more patterns and responses as needed
]
chatbot = Chat(pairs, reflections)
print("Welcome to the chatbot!")
while True:
    user_input = input("You: ")
    response = chatbot.respond(user_input)
    print("Bot:", response)
