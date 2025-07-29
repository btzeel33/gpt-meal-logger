from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return "gpt action endpoint ready"

@app.route('/openai.yaml', methods=['GET'])
def serve_yaml():
    return send_file("openai.yaml", mimetype='text/yaml')

@app.route('/log', methods=['POST'])
def log_meal():
    data = request.json
    meal = data.get("meal")
    print(f"Meal logged: {meal}")
    return jsonify({"message": f"Logged: {meal}"})
