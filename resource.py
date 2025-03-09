import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil

# Track uploaded files for rewards
uploaded_files = []

# Function to upload resources
def upload_resource():
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("All Files", "*.*")])
    if file_path:
        save_path = os.path.join("shared_resources", os.path.basename(file_path))
        os.makedirs("shared_resources", exist_ok=True)
        shutil.copy(file_path, save_path)
        uploaded_files.append(save_path)
        chat_window.insert(tk.END, f"\n📂 Resource Uploaded: {os.path.basename(file_path)}\n", "resource")
        check_badges()

# Function to display badges based on uploads
def check_badges():
    badge_messages = {
        1: "🏅 Congratulations! You've earned the 'First Upload' Badge!",
        5: "🥇 Amazing! You've uploaded 5 resources and earned the 'Contributor' Badge!",
        10: "🌟 Fantastic! You've reached 10 uploads and earned the 'Resource Master' Badge!",
        20: "🏆 Incredible! You've shared 20 resources and earned the 'Mentorship Champion' Badge!"
    }
    if len(uploaded_files) in badge_messages:
        chat_window.insert(tk.END, f"\n{badge_messages[len(uploaded_files)]}\n", "badge")

# Initialize GUI
root = tk.Tk()
root.title("Mentor-Mentee Resource Sharing")

chat_window = tk.Text(root, width=60, height=20, wrap=tk.WORD)
chat_window.pack(padx=10, pady=10)

upload_button = tk.Button(root, text="Upload Resource", command=upload_resource, bg="green", fg="white")
upload_button.pack(pady=5)

chat_window.tag_config("resource", foreground="purple")
chat_window.tag_config("badge", foreground="orange", font=("Helvetica", 10, "bold"))

root.mainloop()
