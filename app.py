from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return '✅ Growth Updater is Live! Visit /run-script to trigger it.'

@app.route('/run-script')
def run_script():
    try:
        result = subprocess.run(['python3', 'growth_update.py'], capture_output=True, text=True)
        return f"<pre>{result.stdout}</pre><br><pre>{result.stderr}</pre>"
    except Exception as e:
        return f"❌ Error running script: {e}"
