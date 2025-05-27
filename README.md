# ReservasAPI

Microsserviço para gerenciar reservas de salas de aula.

## Funcionalidades
- Criar reservas com sala, horário e turma_id
- Listar todas as reservas

## Execução com Docker
```bash
docker-compose up --build
```

Acesse: `http://localhost:5001/reservas`

## Integração
Este microsserviço depende do ID da turma, fornecido pelo Sistema de Gerenciamento (`DEVAPI`).
