import aiml
import time
time.clock = time.time

kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

def get_response(input_text):
    response = kernel.respond(input_text)
    return response

def end_conversation(input_text):
    if input_text.lower() == "goodbye":
        return True
    else:
        return False

print("Hello! I'm Layla, and here to talk to you about depression. Type 'goodbye' to end the conversation.\n")

while True:
    user_input = input("User: ")
    if end_conversation(user_input):
        print("Layla: Goodbye!")
        break
    bot_response = get_response(user_input)
    print("Layla: " + bot_response)