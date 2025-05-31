import uuid
from models.db import db 


class Vengador(db.Model): 
    __tablename__ = 'Vengador' 

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nombre = db.Column(db.String(100), nullable=False)
    alias = db.Column(db.String(100), nullable=True)
    habilidades = db.Column(db.Text, nullable=True) 
    actor = db.Column(db.String(200), nullable=True)


    def __repr__(self):
        # Método para mostrar una representación legible del objeto (útil para debug)
        return f"<Vengador {self.nombre} (id={self.id})>"