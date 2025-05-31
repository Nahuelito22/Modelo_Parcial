# Flask API RESTful CRUD

Este es un proyecto que consiste en una aplicación CRUD usando Flask, SQLAlchemy y MySQL.

## Requisitos

- Python 3
- MySQL

## Configuración del entorno

### 1. Crear un entorno virtual

#### En Linux / macOS:
```sh
python3 -m venv <nombre_del_entorno>
```

#### En Windows:
```sh
python -m venv <nombre_del_entorno>
```

### 2. Activar el entorno virtual

#### En Linux / macOS:
```sh
source <nombre_del_entorno>/bin/activate
```

#### En Windows:
```sh
<nombre_del_entorno>\Scripts\activate
```

### 3. Instalar dependencias

```sh
pip install Flask Flask-SQLAlchemy PyMySQL python-dotenv
```

## Configuración de la base de datos

Antes de ejecutar la aplicación, debes configurar las siguientes variables de entorno:

```sh
MYSQL_USER=<tu_usuario>
MYSQL_PASSWORD=<tu_contraseña>
MYSQL_DATABASE=<nombre_de_la_base_de_datos>
MYSQL_HOST=<host_de_mysql>
```

## Instalación y ejecución

1. Clona el repositorio:
```sh
git clone <url_del_repositorio>
```

2. Accede al directorio del proyecto:
```sh
cd <nombre_del_proyecto>
```

3. Instala las dependencias desde el archivo `requirements.txt`:
```sh
pip install -r requirements.txt
```

4. Ejecuta la aplicación:
```sh
python app.py
```


--------Proyecto Flask - CRUD de Héroes------
Aplicación web simple en Flask para crear, listar, editar y eliminar héroes.

--------Funcionalidades----------
Cargar héroes desde un JSON (avengers.json)

Crear héroes desde frontend (formulario)

Listar y borrar héroes desde vistas HTML

Modelo básico de rutas (GET, POST, PUT, DELETE)

Plantillas con Jinja para mostrar e iterar datos

⚠️ El proyecto está funcional, pero aún quedan ajustes menores, como mejorar los redirects y pulir detalles de navegación.

#Contribuciones#
🛠 Nahuel Ghilardi
Estructura inicial del proyecto Flask

Creación de modelos para la base de datos

Definición de rutas principales (GET, POST, PUT, DELETE) en registroHeroe_routes.py

Generación del seed (avengers.json) con datos de héroes para facilitar pruebas

Pruebas básicas de funcionamiento backend

🎨 Gustavo Garcia
Configuración de la URI de conexión en el módulo de configuración (config/)

Desarrollo de las plantillas HTML con Jinja2 para:

Agregar nuevos héroes (agregar.html)

Listar héroes (listar.html)

Estructura general (layout.html, index.html)

Iteración de datos desde el backend a las vistas

Integración entre frontend y rutas para operar desde la interfaz

Ajustes en el diseño con CSS (main.css)

Organización del proyecto y estructura de carpetas

