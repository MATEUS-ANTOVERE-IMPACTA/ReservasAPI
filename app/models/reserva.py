# app/models/reserva.py

from datetime import datetime
from app.extensions import db

class Reserva(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    turma_id = db.Column(db.Integer, nullable=False)
    aluno_nome = db.Column(db.String(100), nullable=False)
    sala = db.Column(db.String(50), nullable=False)
    horario = db.Column(db.String(50), nullable=False)
    data_reserva = db.Column(db.String(20), default=lambda: datetime.now().strftime('%Y-%m-%d'))

    def to_dict(self):
        return {
            "id": self.id,
            "turma_id": self.turma_id,
            "aluno_nome": self.aluno_nome,
            "sala": self.sala,
            "horario": self.horario,
            "data_reserva": self.data_reserva
        }

    @staticmethod
    def criar(dados):
        nova = Reserva(
            turma_id=dados["turma_id"],
            aluno_nome=dados["aluno_nome"],
            sala=dados["sala"],
            horario=dados["horario"],
            data_reserva=dados.get("data_reserva", datetime.now().strftime('%Y-%m-%d'))
        )
        db.session.add(nova)
        db.session.commit()
        return nova

    @staticmethod
    def listar():
        return Reserva.query.all()

    @staticmethod
    def deletar(id):
        reserva = Reserva.query.get(id)
        if reserva:
            db.session.delete(reserva)
            db.session.commit()
            return True
        return False