# 🧪 SnakeHub: Arquitetura de Microserviços em Python com FastAPI, SQLite e Docker

Este projeto demonstra como construir e executar dois microserviços em Python usando FastAPI, seguindo o padrão CQRS, com banco de dados SQLite e execução em containers com Docker Compose.

---

## 🎯 Problema de Negócio

Gerenciar cupons de desconto promocionais para um e-commerce. O sistema deve permitir:

- Criar novos cupons
- Atualizar e excluir cupons
- Listar todos os cupons
- Buscar cupons por código

---

## 🧱 Arquitetura de Microserviços e Padrão CQRS

Utilizamos dois microserviços:

- `CommandService`: cria, edita e exclui cupons
- `QueryService`: consulta e lista cupons

A arquitetura segue o padrão **CQRS (Command and Query Responsibility Segregation)**, separando leitura e escrita para facilitar manutenção e escalabilidade.

---

## 🌐 Diagrama de Arquitetura

![Diagrama de Arquitetura](./c472b504-d9f3-42a3-ae9b-ceeced61ee62.png)

### Componentes:

- **QueryService (porta 8080)**  
  Rotas:
  - `GET /api/cupons`
  - `GET /api/cupons/{code}`  
  Arquivo: `QueryService/main.py`

- **CommandService (porta 8081)**  
  Rotas:
  - `POST /api/cupons`
  - `PUT /api/cupons/{id}`
  - `DELETE /api/cupons/{id}`  
  Arquivo: `CommandService/main.py`

- **Shared** (reaproveitado por ambos):
  - `shared/models/cupom.py`: estrutura dos dados
  - `shared/database.py`: inicialização e conexão com SQLite

---

## 📂 Estrutura do Projeto

```
project/
├── docker-compose.yml
├── Dockerfile.command
├── Dockerfile.query
├── shared/
│   ├── database.py
│   └── models/
│       ├── __init__.py
│       └── cupom.py
├── CommandService/
│   └── main.py
└── QueryService/
    └── main.py
```

---

## ⚙️ Como executar

### 1. Criar ambiente virtual (opcional)
```bash
python -m venv snakehub
source snakehub/bin/activate  # No Windows: snakehub\Scripts\activate
```

### 2. Subir os serviços com Docker
```bash
docker-compose up --build
```

### 3. Testar no navegador
- http://localhost:8080/docs → consultas
- http://localhost:8081/docs → criação, edição, exclusão

---

## 📜 Licença

Este projeto é livre para fins de aprendizado, estudos e extensões acadêmicas.