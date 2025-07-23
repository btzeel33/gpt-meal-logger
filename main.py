from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "GPT Action endpoint ready"

@app.route("/log-meal", methods=["POST"])
def log_meal():
    data = request.get_json()
    print("Meal data received:", data)
    return jsonify({"message": "Meal logged successfully", "data": data})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
