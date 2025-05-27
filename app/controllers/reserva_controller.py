from flask import Blueprint, request, jsonify
from app.models.reserva import Reserva

reserva_bp = Blueprint('reserva_bp', __name__)

@reserva_bp.route('', methods=['GET'])
def listar_reservas():
    return jsonify(Reserva.listar())

@reserva_bp.route('', methods=['POST'])
def criar_reserva():
    data = request.get_json()
    resposta, status = Reserva.criar(data)
    return jsonify(resposta), status
