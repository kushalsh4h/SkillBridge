import tkinter as tk

# Sample mentor and mentee data
mentors = [
    {"name": "Alice", "goals": "Career Growth", "interests": "AI, Machine Learning", "background": "Software Engineer"},
    {"name": "Bob", "goals": "Skill Development", "interests": "Cybersecurity, Networking", "background": "Security Analyst"},
    {"name": "Charlie", "goals": "Project Guidance", "interests": "Web Development, UI/UX", "background": "Frontend Developer"}
]

# Function to match mentees with mentors
def find_mentor():
    goal = goal_entry.get().lower()
    interest = interest_entry.get().lower()
    background = background_entry.get().lower()
    matches = []
    
    for mentor in mentors:
        if (goal in mentor["goals"].lower() or interest in mentor["interests"].lower() or background in mentor["background"].lower()):
            matches.append(f"👤 {mentor['name']} - {mentor['background']}\n   🎯 Goals: {mentor['goals']}\n   📌 Interests: {mentor['interests']}\n")
    
    result_window.insert(tk.END, "\n🔍 Matching Mentors:\n" + ("\n".join(matches) if matches else "No matches found."), "match")

# Initialize GUI
root = tk.Tk()
root.title("Mentor Matching System")

result_window = tk.Text(root, width=60, height=15, wrap=tk.WORD)
result_window.pack(padx=10, pady=10)

# Mentor Search Fields
tk.Label(root, text="Search for a Mentor").pack()
goal_entry = tk.Entry(root, width=40)
goal_entry.pack()
tk.Label(root, text="Enter Goals").pack()
interest_entry = tk.Entry(root, width=40)
interest_entry.pack()
tk.Label(root, text="Enter Interests").pack()
background_entry = tk.Entry(root, width=40)
background_entry.pack()
tk.Label(root, text="Enter Professional Background").pack()

search_button = tk.Button(root, text="Find Mentor", command=find_mentor, bg="blue", fg="white")
search_button.pack(pady=5)

result_window.tag_config("match", foreground="blue", font=("Helvetica", 10, "bold"))

root.mainloop()
