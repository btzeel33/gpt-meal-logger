
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)
log = []

@app.route('/')
def home():
    return "GPT Action Endpoint Ready"

@app.route('/log', methods=['POST'])
def log_meal():
    data = request.json
    meal = data.get('meal')
    carbs = data.get('carbs')
    timestamp = data.get('timestamp', datetime.utcnow().isoformat())

    entry = {
        "meal": meal,
        "carbs": carbs,
        "timestamp": timestamp
    }

    log.append(entry)

    print("🔥 GPT Action Triggered — Meal Logged!")
    print("Logged Entry:")
    print(entry)
    print("Full Log:")
    print(log)
    print("────────────────────────────────────────")

    return jsonify({"status": "success", "log": log}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
