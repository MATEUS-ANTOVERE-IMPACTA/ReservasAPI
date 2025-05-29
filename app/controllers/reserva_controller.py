from flask import Blueprint, request, jsonify
from flasgger import swag_from
from ..models.reserva import Reserva

reserva_bp = Blueprint("reserva", __name__)

@reserva_bp.route("/", methods=["GET"])
@swag_from({...})  # pode manter como você já tinha feito
def listar():
    reservas = Reserva.listar()
    return jsonify([r.to_dict() for r in reservas]), 200

@reserva_bp.route("/", methods=["POST"])
@swag_from({...})  # idem
def criar():
    dados = request.get_json()
    reserva = Reserva.criar(dados)
    return jsonify(reserva.to_dict()), 201

@reserva_bp.route("/<int:id>", methods=["DELETE"])
@swag_from({...})  # idem
def deletar(id):
    sucesso = Reserva.deletar(id)
    if sucesso:
        return jsonify({"mensagem": "Reserva deletada com sucesso"}), 200
    return jsonify({"erro": "Reserva não encontrada"}), 404