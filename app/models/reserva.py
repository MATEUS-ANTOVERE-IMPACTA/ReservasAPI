from datetime import datetime
from app.extensions import db  # e não mais de config

class Reserva(db.Model):
    __tablename__ = 'reservas'

    id = db.Column(db.Integer, primary_key=True)
    turma_id = db.Column(db.Integer, nullable=False)
    data_reserva = db.Column(db.String(50), nullable=False, default=datetime.now().strftime("%Y-%m-%d"))
    aluno_nome = db.Column(db.String(100), nullable=False)
    sala = db.Column(db.String(100), nullable=False)
    horario = db.Column(db.String(100), nullable=False)

    @staticmethod
    def criar(dados):
        nova = Reserva(**dados)
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

    def to_dict(self):
        return {
            "id": self.id,
            "turma_id": self.turma_id,
            "data_reserva": self.data_reserva,
            "aluno_nome": self.aluno_nome,
            "sala": self.sala,
            "horario": self.horario
        }