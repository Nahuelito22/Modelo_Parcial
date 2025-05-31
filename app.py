# app.py
# Importamos librerias, rutas y modelos
from flask import Flask , render_template
from config.config import Config 
from models.db import db
from routes.registroHeroe_routes import heroes_bp # Importa el Blueprint correctamente

app = Flask(__name__)

def create_app():
    """
    Función para crear y configurar la aplicación Flask.
    """
    app.config.from_object(Config)
    db.init_app(app)
    
    with app.app_context():
        # db.drop_all() 
        db.create_all() 

    app.register_blueprint(heroes_bp, url_prefix="/vengador") 
    
    return app

# Ruta principal para visualizar el index 
@app.route("/")
def index():
    return render_template("index.html")


if __name__=="__main__":
    # Si este archivo se ejecuta directamente, creamos la app y la iniciamos
    app = create_app()
    app.run(debug=True) 