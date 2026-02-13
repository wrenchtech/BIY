from app import db
from flask_login import UserMixin


class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    rol = db.Column(db.String(20), nullable=False)  # admin o paciente

    cliente = db.relationship("Cliente", backref="usuario", uselist=False)


class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    email = db.Column(db.String(100))
    telefono = db.Column(db.String(20))

    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"))
