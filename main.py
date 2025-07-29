from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'GPT action endpoint ready'

@app.route('/log', methods=['POST'])
def log():
    data = request.get_json()
    meal = data.get('meal', 'Unknown meal')
    print(f"Logged meal: {meal}")
    return jsonify({"message": f"Logged your meal: {meal}"})
