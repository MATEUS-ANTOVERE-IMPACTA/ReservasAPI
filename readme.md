# 📅 ReservasAPI - Sistema de Gerenciamento de Reservas de Salas

O **ReservasAPI** é um microsserviço RESTful desenvolvido em **Python com Flask**, especializado em registrar e gerenciar reservas de salas realizadas por turmas.

Segue o padrão arquitetural **MVC**, utiliza banco de dados **SQLite**, e está integrado com **Swagger UI** para documentação interativa e testes simplificados.

---

## 🚀 Funcionalidades

### 📌 Cadastro de Reservas
Cada reserva inclui:

- Nome do aluno
- Turma
- Sala
- Horário
- Data da reserva

Validações essenciais para garantir integridade dos dados (ex: campos obrigatórios).

### 📄 Listagem de Reservas

Visualização completa de todas as reservas registradas no sistema.

### 🧾 Documentação com Swagger UI

- Interface gráfica para testar e visualizar rotas.
- Disponível em: [http://localhost:5001/apidocs](http://localhost:5001/apidocs)

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.11**
- **Flask 3.0.2**
- **Flask-SQLAlchemy**
- **Flasgger (Swagger UI)**
- **SQLite**
- **Docker & Docker Compose**

---

## 🐳 Como Rodar com Docker

Clone o repositório:

```bash
git clone https://github.com/MATEUS-ANTOVERE-IMPACTA/ReservasAPI
cd ReservasAPI
Execute via Docker Compose:

bash
Copiar
Editar
docker-compose up --build
🌐 Acesse a aplicação
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
POST /reservas – Criar nova reserva.

GET /reservas – Listar todas as reservas.

👨‍💻 Equipe de Desenvolvimento
Mateus Antovere Silva Rosário | RA: 2401764

Leandro Ferreira Cassemiro Rosa | RA: 2302060

Gabriel Quaglio Monteiro Praça | RA: 2400738
