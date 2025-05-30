import uuid
import os
from werkzeug.utils import secure_filename
from flask import Blueprint, flash, redirect, render_template, request, jsonify, abort
from models.registroHeroe import Vengador
from models.db import db

# Creamos el blueprint para Vengador
heroes_bp = Blueprint(' heroes_bp', __name__)

# GET / Obtener todas las vos vengadores    
@heroes_bp.route("/", methods=["GET"])
def get_all_vengadores():
    try:
        # Obtenemos todos los registros de la tabla Vengador
        vengadores = Vengador.query.all()
        return render_template("vengadores.html", vengadores=vengadores)
    except Exception as e:
        print(f"Error al obtener los vengadores: {e}")
        abort(500)

# Get / Obtener un vengador por ID
@heroes_bp.route("/<string:id>", methods=["GET"])   
def get_vengador(id):
    try:
        # Buscamos el vengador por ID
        vengador = Vengador.query.get_or_404(id)
        return render_template("vengador.html", vengador=vengador)
    except Exception as e:
        print(f"Error al obtener el vengador: {e}")
        abort(500)

# POST / Crear un nuevo vengador
@heroes_bp.route("/", methods=["POST"])         

def create_vengador():
    try:
        # Obtenemos los datos del formulario
        nombre = request.form.get("nombre")
        alias = request.form.get("alias")
        habilidades = request.form.get("habilidades")
        actor = request.form.get("actor")

        # Validamos que se hayan proporcionado los campos obligatorios
        if not nombre or not alias:
            flash("Nombre y alias son obligatorios", "error")
            return redirect(request.referrer)

        # Creamos una nueva instancia de Vengador
        nuevo_vengador = Vengador(
            id=str(uuid.uuid4()),  # Generamos un ID único
            nombre=nombre,
            alias=alias,
            habilidades=habilidades,
            actor=actor
        )

        # Agregamos el nuevo vengador a la sesión y lo guardamos en la base de datos
        db.session.add(nuevo_vengador)
        db.session.commit()

        flash("Vengador creado exitosamente", "success")
        return redirect("/vengadores")  # Redirigimos a la lista de vengadores
    except Exception as e:
        print(f"Error al crear el vengador: {e}")
        flash("Error al crear el vengador", "error")
        return redirect(request.referrer)
