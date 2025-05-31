# seed.py
import json
import uuid
from pathlib import Path
from app import create_app 
from models.db import db
from models.registroHeroe import Vengador 


def seed_database():
    """
    Carga datos desde avengers.json y los inserta en la base de datos.
    """
    app = create_app() # Creamos una instancia de la app para obtener el contexto
    
    with app.app_context():
        # Ruta al archivo JSON
        
        JSON_FILE_PATH = Path(__file__).parent / "avengers.json"

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
                            id=str(uuid.uuid4()), 
                            nombre=hero_data.get("nombre"),
                            alias=hero_data.get("alias"),
                            habilidades=str(hero_data.get("habilidades")), 
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

if __name__ == '__main__':
    seed_database()