from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)
log = []

@app.route('/log', methods=['POST'])
def log_meal():
    data = request.json
    meal = data.get('meal')
    carbs = data.get('carbs')
    timestamp = data.get('timestamp', datetime.utcnow().isoformat())

    log.append({
        "meal": meal,
        "carbs": carbs,
        "timestamp": timestamp
    })

    print(log)
    return jsonify({"status": "success", "log": log}), 200

@app.route('/')
def home():
    return "GPT Action Endpoint Ready"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    from flask import Flask, request, jsonify
    from datetime import datetime

    app = Flask(__name__)
    log = []

    @app.route('/log', methods=['POST'])
    def log_meal():
        data = request.json
        meal = data.get('meal')
        carbs = data.get('carbs')
        timestamp = data.get('timestamp', datetime.utcnow().isoformat())

        log.append({
            "meal": meal,
            "carbs": carbs,
            "timestamp": timestamp
        })

        print(log)
        return jsonify({"status": "success", "log": log}), 200

    @app.route('/')
    def home():
        return "GPT Action Endpoint Ready"

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8080)
