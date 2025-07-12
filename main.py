"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

# Fullscreen the canvas
screen = turtle.Screen()
screen.setup(1.0, 1.0)

# Begin!
t = turtle.Turtle()

for c in ['red', 'green', 'blue', 'yellow']:
  t.color(c)
  t.forward(75)
  t.left(90)

screen.mainloop()
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
