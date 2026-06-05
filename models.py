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

class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    perfil = db.Column(db.Text, nullable=False)
    problema = db.Column(db.Text, nullable=False)