from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Card, Collection
import json, os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "instance", "tcg.db")
db.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/cards")
def get_cards():
    cards = Card.query.all()
    cards_list = []
    for card in cards:
        cards_list.append({
            "id": card.id,
            "name": card.name,
            "mana_cost": card.mana_cost,
            "cmc": card.cmc,
            "type_line": card.type_line,
            "oracle_text": card.oracle_text,
            "power": card.power,
            "toughness": card.toughness
        })
    return jsonify(cards_list)


@app.route("/view_cards")
def view_cards():
    cards = Card.query.all()
    return render_template("view_cards.html", cards=cards)

@app.route("/card/<int:card_id>")
def view_card(card_id):
    card = Card.query.get_or_404(card_id)
    return jsonify(card)


@app.route("/get_card_details", methods=["POST"])
def get_card_details():
    data = request.json
    card_class = data.get("className")

    card = Card.query.filter_by(class_id=card_class).first()
    card_info = card.make_json() if card else None

    if card_info:
        return jsonify({"success": True, "card": card_info})
    return jsonify({"success": False, "error": "Card not found"}), 404


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0")
