from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    collection_items = db.relationship("Collection", backref="owner", lazy=True)


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    mana_cost = db.Column(db.String(50))
    cmc = db.Column(db.Integer)
    type_line = db.Column(db.String(100))
    oracle_text = db.Column(db.Text)
    power = db.Column(db.String(10))
    toughness = db.Column(db.String(10))
    class_id = db.Column(db.String(50), unique=True)

    in_collections = db.relationship("Collection", backref="card_data", lazy=True)


class Collection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    card_id = db.Column(db.Integer, db.ForeignKey("card.id"), nullable=False)

    # Extra fields specific to the user's copy of the card
    quantity = db.Column(db.Integer, default=1)
    is_foil = db.Column(db.Boolean, default=False)