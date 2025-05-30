import uuid
from models.db import db  

class VariedadUva(db.Model):
    __tablename__ = 'Vengador'  # Nombre explícito para la tabla en la base de datos

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nombre = db.Column(db.String(100), nullable=False)
    alias = db.Column(db.String(100), nullable=True)
    habilidades = db.Column(db.String(100), nullable=True)
    actor = db.Column(db.String(200), nullable=True)

    

    def __repr__(self):
        # Método para mostrar una representación legible del objeto (útil para debug)
        return f"<VariedadUva {self.nombre} (id={self.id})>"