from flask import Flask, jsonify, render_template, request
import json

app = Flask(__name__)

card_data = {}
with open("static/card_data.json", "r") as f:
    card_data = json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cards")
def get_cards():
    return jsonify(card_data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
