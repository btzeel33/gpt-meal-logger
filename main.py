from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

@app.route("/log", methods=["POST"])
def log_meal():
    data = request.get_json()
    meal = data.get("meal", "")
    print(f"Meal logged: {meal}")
    return jsonify({"status": "Meal successfully logged!"})

@app.route("/openapi.yaml", methods=["GET"])
def serve_openapi():
    return send_from_directory(".", "openapi.yaml", mimetype="text/yaml")

@app.route("/", methods=["GET"])
def home():
    return "GPT Action endpoint ready"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)