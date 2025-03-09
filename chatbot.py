import random
import nltk
import tkinter as tk
import webbrowser  # To open Jitsi Meet in a browser
from nltk.chat.util import Chat, reflections

# Define patterns and responses
pairs = [
    [r"hi|hello|hey", ["Hello! How can I assist you today?", "Hi there! What can I do for you?"]],
    [r"how are you", ["I'm just a bot, but I'm here to help!", "I'm doing great! How can I assist you?"]],
    [r"what is mentorship", ["Mentorship is a relationship where a more experienced person helps guide a less experienced person in their personal or professional development."]],
    [r"benefits of mentorship", ["Mentorship helps in career growth, skill development, networking, and gaining new perspectives."]],
    [r"how to find a mentor", ["You can find a mentor by joining mentorship programs, networking events, or professional platforms like LinkedIn."]],
    [r"quit|exit|bye", ["Goodbye! Have a great day!", "Bye! Take care!"]],
    [r"(.*)", ["I'm not sure about that. Can you rephrase your question?", "Could you clarify your question?"]]
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# GUI Application
def send_message():
    user_input = user_entry.get()
    if user_input.lower() in ["quit", "exit", "bye"]:
        chat_window.insert(tk.END, "You: " + user_input + "\n")
        chat_window.insert(tk.END, "Chatbot: Goodbye!\n")
        root.quit()
    else:
        response = chatbot.respond(user_input)
        chat_window.insert(tk.END, "You: " + user_input + "\n", "user")
        chat_window.insert(tk.END, "Chatbot: " + response + "\n", "bot")
    user_entry.delete(0, tk.END)

# Function to start a video call
def start_video_call():
    jitsi_meet_url = "https://meet.jit.si/MentorMenteeChat"
    webbrowser.open(jitsi_meet_url)

# Initialize GUI
root = tk.Tk()
root.title("Mentor-Mentee Chatbot")

chat_window = tk.Text(root, width=50, height=20, wrap=tk.WORD)
chat_window.pack(padx=10, pady=10)

user_entry = tk.Entry(root, width=40)
user_entry.pack(padx=10, pady=5)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

video_call_button = tk.Button(root, text="Start Video Call", command=start_video_call, bg="blue", fg="white")
video_call_button.pack(pady=5)

chat_window.tag_config("user", foreground="blue")
chat_window.tag_config("bot", foreground="green")

root.mainloop()
