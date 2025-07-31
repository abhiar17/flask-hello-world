from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/run-script', methods=['GET'])
def run_script():
    try:
        result = subprocess.run(["python3", "growth_update.py"], capture_output=True, text=True, check=True)
        return f"✅ Script executed:\n\nOutput:\n{result.stdout}\n\n⚠️ Errors (if any):\n{result.stderr}"
    except subprocess.CalledProcessError as e:
        return f"❌ Script failed:\n\n{e.output}\n\n{e.stderr}"

if __name__ == '__main__':
    app.run(debug=True)
