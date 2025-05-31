# app.py
# Importamos librerias, rutas y modelos
from flask import Flask , render_template
from config.config import Config 
from models.db import db
from models import registroHeroe
from routes.registroHeroe_routes import heroes_bp

app = Flask(__name__)

def create_app():
    """
    Función para crear y configurar la aplicación Flask.
    """
    app.config.from_object(Config)
    db.init_app(app)
    
    with app.app_context():
        #db.drop_all() #borra todo 
        db.create_all()  # Aquí se crean las tablas si no existen
    
    # Registramos los blueprints
    app.register_blueprint(heroes_bp, url_prefix="/heroes") # Se usa el url_prefix para acortar la ruta en routes y definirla directamente aca

    # app.register_blueprint(heroes_bp, url_prefix="/vengador") 
    
    return app

# Ruta principal para visualizar el index 
@app.route("/")
def index():
    return render_template("index.html")


if __name__=="__main__":
    # Si este archivo se ejecuta directamente, creamos la app y la iniciamos
    app = create_app()
    app.run(debug=True) 