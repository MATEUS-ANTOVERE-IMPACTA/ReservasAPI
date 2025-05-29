from flask import Blueprint, request, jsonify
from flasgger import swag_from
from ..models.reserva import Reserva

reserva_bp = Blueprint("reserva", __name__)

@reserva_bp.route("/", methods=["GET"])
@swag_from({
    'tags': ['Reservas'],
    'responses': {
        200: {
            'description': 'Lista de reservas',
            'examples': {
                'application/json': [
                    {
                        "id": 1,
                        "turma_id": 2,
                        "data_reserva": "2025-05-26",
                        "aluno_nome": "Carlos",
                        "sala": "101A",
                        "horario": "14:00"
                    }
                ]
            }
        }
    }
})
def listar():
    try:
        reservas = Reserva.listar()
        return jsonify([r.to_dict() for r in reservas]), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@reserva_bp.route("/", methods=["POST"])
@swag_from({
    'tags': ['Reservas'],
    'parameters': [{
        'name': 'body',
        'in': 'body',
        'required': True,
        'schema': {
            'type': 'object',
            'properties': {
                'turma_id': {'type': 'integer'},
                'data_reserva': {'type': 'string'},
                'aluno_nome': {'type': 'string'},
                'sala': {'type': 'string'},
                'horario': {'type': 'string'}
            },
            'required': ['turma_id', 'aluno_nome', 'sala', 'horario']
        }
    }],
    'responses': {
        201: {'description': 'Reserva criada com sucesso'},
        400: {'description': 'Erro ao criar reserva'}
    }
})
def criar():
    try:
        dados = request.get_json()
        reserva = Reserva.criar(dados)
        return jsonify(reserva.to_dict()), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@reserva_bp.route("/<int:id>", methods=["DELETE"])
@swag_from({
    'tags': ['Reservas'],
    'parameters': [{
        'name': 'id',
        'in': 'path',
        'type': 'integer',
        'required': True
    }],
    'responses': {
        200: {'description': 'Reserva deletada com sucesso'},
        404: {'description': 'Reserva não encontrada'}
    }
})
def deletar(id):
    sucesso = Reserva.deletar(id)
    if sucesso:
        return jsonify({"mensagem": "Reserva deletada com sucesso"}), 200
    return jsonify({"erro": "Reserva não encontrada"}), 404