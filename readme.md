# 🗓️ ReservasAPI - Sistema de Gerenciamento de Reservas de Salas

A **ReservasAPI** é um microsserviço RESTful em **Python com Flask**, responsável por registrar as **reservas de salas feitas por turmas**. A aplicação segue o padrão **MVC**, utiliza **SQLite**, e está integrada à documentação **Swagger** para facilitar testes e visualização de endpoints.

---

## 🚀 Funcionalidades

- 📝 **Cadastro de Reservas**
  - Cada reserva inclui: nome do aluno, turma, sala, horário e data da reserva.
  - Validações básicas de integridade (ex: campo obrigatório).

- 📄 **Listagem de Reservas**
  - Exibe todas as reservas registradas no banco de dados.

- 🧾 **Swagger UI**
  - Interface visual para explorar e testar as rotas.
  - Disponível em: [`/apidocs`](http://localhost:5001/apidocs)

---

## 🛠️ Tecnologias Utilizadas

- Python 3.11
- Flask 3.0.2
- Flask-SQLAlchemy
- Flasgger (Swagger UI)
- SQLite
- Docker & Docker Compose

---

## 🐳 Como Rodar com Docker

1. Clone o repositório:
   ```bash
   git clone https://github.com/MATEUS-ANTOVERE-IMPACTA/ReservasAPI
   cd ReservasAPI
Execute via Docker:

bash
Copiar
Editar
docker-compose up --build
Acesse:

Swagger UI: http://localhost:5001/apidocs

API: http://localhost:5001

📂 Estrutura do Projeto
arduino
Copiar
Editar
ReservasAPI/
├── app/
│   ├── controllers/
│   │   └── reserva_controller.py
│   ├── models/
│   │   └── reserva.py
│   ├── __init__.py
│   └── app.py
├── config.py
├── extensions.py
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
📡 Endpoints Principais
POST /reservas – Criar uma nova reserva

GET /reservas – Listar todas as reservas

👨‍💻 Desenvolvido por
👤 Mateus Antovere Silva Rosário | RA: 2401764
👤 Leandro Ferreira Cassemiro Rosa | RA: 2302060
👤 Gabriel Quaglio Monteiro Praça | RA: 2400738