# app.py
import json 
import uuid 
from pathlib import Path 
from flask import Flask , render_template
from config.config import Config 
from models.db import db
from models.registroHeroe import Vengador
from routes.registroHeroe_routes import heroes_bp 


# Creamos la app, configuraciones e importaciones
app = Flask(__name__)

# Definimos la ruta al archivo JSON

JSON_FILE_PATH = Path(__file__).parent / "avengers.json"

def create_app():
    
    # Cargamos la configuracion
    app.config.from_object(Config)
    
    # Inicializamos base de datos
    db.init_app(app)
    
    with app.app_context():
        # db.drop_all() # Para borrar todo en testint
        db.create_all() 

        # AQUI ES DONDE CARGAMOS EL JSON Y POBLAMOS LA BASE DE DATOS 
        try:
            # Solo poblar si la tabla Vengador está vacía
            if Vengador.query.count() == 0:
                print(f"[{__name__}] La tabla Vengador está vacía. Procediendo a cargar datos desde avengers.json...")
                with open(JSON_FILE_PATH, "r", encoding="utf-8") as f:
                    data_from_json = json.load(f)
                    avengers_list = data_from_json.get("avengers", []) 
                
                if avengers_list:
                    for hero_data in avengers_list:
            
                        new_vengador = Vengador(
                            id=str(uuid.uuid4()), # Genera un ID único para cada vengador
                            nombre=hero_data.get("nombre"),
                            alias=hero_data.get("alias"),
                            habilidades=str(hero_data.get("habilidades")), # Convertir la lista a string para la DB
                            actor=hero_data.get("actor")
                        )
                        db.session.add(new_vengador)
                    
                    db.session.commit()
                    print(f"[{__name__}] Datos de 'avengers.json' cargados y agregados a la base de datos. Total de vengadores: {Vengador.query.count()}")
                else:
                    print(f"[{__name__}] El archivo 'avengers.json' está vacío o no contiene la clave 'avengers'.")
            else:
                print(f"[{__name__}] La tabla Vengador ya contiene datos. No se cargó 'avengers.json'.")
        except FileNotFoundError:
            print(f"[{__name__}] Advertencia: El archivo '{JSON_FILE_PATH.name}' no se encontró en '{JSON_FILE_PATH}'. No se cargaron datos iniciales.")
        except json.JSONDecodeError:
            print(f"[{__name__}] Error: No se pudo decodificar el JSON de '{JSON_FILE_PATH.name}'. Revisa su formato.")
        except Exception as e:
            print(f"[{__name__}] Ocurrió un error inesperado al cargar o insertar datos de 'avengers.json': {e}")
        # FIN DE LA CARGA DEL JSON
        
    # Registramos los blueprints
    # Asegúrate de que 'heroes_bp' es el nombre que usaste en registroHeroe_routes.py
    app.register_blueprint(heroes_bp, url_prefix="/vengador")
    
    return app

#visualizamos index
@app.route("/")
def index():
    return render_template("index.html")


if __name__=="__main__":
    app = create_app()
    app.run(debug=True)