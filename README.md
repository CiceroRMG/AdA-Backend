# AdA-backend

Este projeto é construído com python e fastAPI

## Pré-requisitos

- Docker
- (Recomendado) Docker Compose

## Como rodar o projeto

### Rodando localmente

1. Crie um ambiente virtual: `python -m venv venv`
2. Ative o ambiente virtual:
   - No Windows: `venv\Scripts\activate`
   - No Unix ou MacOS: `source venv/bin/activate`
3. Instale as dependências: `pip install -r requirements.txt`
4. Execute o script de configuração: `pip install -e .`
5. Inicie o servidor: `uvicorn src.main:app --reload`
6. Acesse http://localhost:8000 para verificar o funcionamento

### Rodando com Docker

1. Instale o Docker e o Docker Compose
2. Execute `docker-compose up --build` para iniciar a aplicação
3. Acesse http://localhost:8000 para verificar o funcionamento
