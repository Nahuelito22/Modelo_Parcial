from dotenv import load_dotenv
import os

<<<<<<< HEAD
load_dotenv()

user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
host = os.getenv("MYSQL_HOST")
database = os.getenv("MYSQL_DB")

DATABASE_CONNECTION_URI = f"mysql+pymysql://{user}:{password}@{host}/{database}"
=======
# Cargar variables del archivo .env
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "claveporDefecto")
    
    # Armamos la URI de conexión a MySQL desde el .env
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_DB = os.getenv("MYSQL_DB")

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
>>>>>>> 61dcdb88c8aab737b8a0722d984639d23d69b880
