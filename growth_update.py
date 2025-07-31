from flask import Flask, jsonify, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return "Growth updater is live!"

@app.route('/run', methods=['POST'])
def run_script():
    try:
        result = subprocess.run(['python3', 'growth_update.py'], capture_output=True, text=True)
        return jsonify({
            "status": "success",
            "stdout": result.stdout,
            "stderr": result.stderr
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
