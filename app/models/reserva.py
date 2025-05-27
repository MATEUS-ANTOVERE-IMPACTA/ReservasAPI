from app import db
import requests

class Reserva(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sala = db.Column(db.String(100), nullable=False)
    horario = db.Column(db.String(20), nullable=False)
    turma_id = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "sala": self.sala,
            "horario": self.horario,
            "turma_id": self.turma_id
        }

    @staticmethod
    def criar(data):
        campos = ['sala', 'horario', 'turma_id']
        for campo in campos:
            if campo not in data:
                return {"erro": f"Campo ausente: {campo}"}, 400

        # Verificação se a turma existe na DEVAPI
        try:
            r = requests.get(f"http://localhost:5000/turmas/{data['turma_id']}")
            if r.status_code != 200:
                return {"erro": "Turma não encontrada na DEVAPI"}, 400
        except requests.exceptions.ConnectionError:
            return {"erro": "Erro ao conectar com o DEVAPI"}, 500

        reserva = Reserva(**data)
        db.session.add(reserva)
        db.session.commit()
        return reserva.to_dict(), 201

    @staticmethod
    def listar():
        return [r.to_dict() for r in Reserva.query.all()]