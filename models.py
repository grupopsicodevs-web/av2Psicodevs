from config import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(300))


class Checkin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    humor = db.Column(db.String(50))


class Diario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.Text)