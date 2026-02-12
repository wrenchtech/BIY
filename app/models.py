from datetime import datetime
from app import db

class Cliente(db.Model):
    __tablename__ = "clientes"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120))
    telefono = db.Column(db.String(20))
    objetivo = db.Column(db.String(50))
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    estado = db.Column(db.String(50), default="Activo")

    def __repr__(self):
        return f"<Cliente {self.nombre}>"
