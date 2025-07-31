from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Flask app is live!"

@app.route('/run-script')
def run_script():
    try:
        result = subprocess.run(['python3', 'growth_update.py'], capture_output=True, text=True)
        return f"✅ Script executed:<br><br><pre>{result.stdout}</pre><br>⚠️ Errors (if any):<br><pre>{result.stderr}</pre>"
    except Exception as e:
        return f"❌ Failed to run script: {e}"
