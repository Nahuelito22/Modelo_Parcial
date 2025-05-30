import uuid
import os
from werkzeug.utils import secure_filename
from flask import Blueprint, flash, redirect, render_template, request, jsonify, abort
from models.registroHeroe import Vengador
from models.db import db

# Creamos el blueprint para Vengador
variedadUva_bp = Blueprint(' Vengador_bp', __name__)
