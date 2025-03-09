from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/start-chatbot', methods=['GET'])
def start_chatbot():
    try:
        subprocess.Popen(["python", "chatbot.py"])  # Runs chatbot.py
        return "Chatbot started!", 200
    except Exception as e:
        return str(e), 500

@app.route('/start-carrerpath', methods=['GET'])
def start_career_script():
    try:
        subprocess.Popen(["python", "carrerpath.py"])  # Runs carrerpath.py
        return "Career Path script started!", 200
    except Exception as e:
        return str(e), 500

@app.route('/start-resource', methods=['GET'])
def start_resource_script():
    try:
        subprocess.Popen(["python", "resource.py"])  # Runs resource.py
        return "Resource script started successfully!", 200
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
