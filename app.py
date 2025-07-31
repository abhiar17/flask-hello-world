from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/run-script')
def run_script():
    try:
        output = subprocess.check_output(["python3", "growth_update.py"], stderr=subprocess.STDOUT)
        return f"<pre>{output.decode()}</pre>"
    except subprocess.CalledProcessError as e:
        return f"<pre>Error:\n{e.output.decode()}</pre>", 500
