import tkinter as tk

# Sample career paths based on courses
career_paths = {
    "AI & Machine Learning": "🔹 Start with Python & Math basics\n🔹 Learn Machine Learning & Deep Learning\n🔹 Work on real-world AI projects\n🔹 Apply for AI Researcher, Data Scientist roles",
    "Cybersecurity": "🔹 Learn networking fundamentals\n🔹 Understand ethical hacking & security protocols\n🔹 Get certified (CEH, CISSP)\n🔹 Apply for Security Analyst, Penetration Tester roles",
    "Web Development": "🔹 Master HTML, CSS, JavaScript\n🔹 Learn Frontend & Backend frameworks\n🔹 Build full-stack applications\n🔹 Apply for Frontend, Backend, or Full-Stack Developer roles"
}

# Function to suggest career path
def suggest_career():
    selected_course = course_entry.get()
    career_info = career_paths.get(selected_course, "No career path found for this course.")
    result_window.insert(tk.END, f"\n📘 Career Path for {selected_course}:\n{career_info}\n", "career")

# Initialize GUI
root = tk.Tk()
root.title("Career Path Suggester")

result_window = tk.Text(root, width=60, height=15, wrap=tk.WORD)
result_window.pack(padx=10, pady=10)

# Course Selection
tk.Label(root, text="Enter Course Name:").pack()
course_entry = tk.Entry(root, width=40)
course_entry.pack()

tk.Button(root, text="Get Career Path", command=suggest_career, bg="green", fg="white").pack(pady=5)

result_window.tag_config("career", foreground="blue", font=("Helvetica", 10, "bold"))

root.mainloop()
