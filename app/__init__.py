# app/__init__.py
from flask import Flask, jsonify
from flasgger import Swagger
from .extensions import db  # CORRETO agora
from .config import DATABASE_URI, TRACK_MODIFICATIONS
from .controllers.reserva_controller import reserva_bp

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = TRACK_MODIFICATIONS
    app.config["SWAGGER"] = {
        "title": "Reservas API - Documentação Swagger",
        "uiversion": 3
    }

    db.init_app(app)  # ESSENCIAL
    Swagger(app)
    app.register_blueprint(reserva_bp, url_prefix="/reservas")

    @app.route("/")
    def index():
        return jsonify({"mensagem": "Bem-vindo à API de Reservas! Acesse /apidocs/ para ver a documentação."})

    with app.app_context():
        db.create_all()

    return app