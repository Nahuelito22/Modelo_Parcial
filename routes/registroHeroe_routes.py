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

