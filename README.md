# AdA-backend

Este projeto é construído com python e fastAPI, utilizando Postgre como banco de dados.

## Pré-requisitos

- Docker instalado
- (Recomendado) Docker Compose
- Se estiver usando windows ou mac não esqueça de abrir o Docker Desktop

## Como rodar o projeto

### Configure as variáveis de ambiente
- Crie o arquivo .env na raiz
- Copie o conteúdo de .env.example e cole em .env

### Rodando com Docker

1. Navegue até a pasta do projeto e execute:
   ```
   `docker compose up --build`
   ```
2. Acesse http://localhost:8000 para verificar o funcionamento

### Rodando localmente

Para rodar localmente, o banco de dados deve estar funcionando seguindo um desses passos:
   - na variável DATABASE_URL no arquivo .env, coloque a URL do seu banco de dados postgre local/nuvem;
   - ou rode docker compose up -d para criar o container do banco de dados (requer docker compose).

É necessário ter o python instalado para seguir esta etapa

Após se certificar que o banco de dados está disponível, siga estes passos:
1. Crie um ambiente virtual: `python -m venv venv`
2. Ative o ambiente virtual:
   - No Windows: `venv\Scripts\activate`
   - No Unix ou MacOS: `source venv/bin/activate`
3. Instale as dependências: `pip install -r requirements.txt`
4. Execute o script de configuração: `pip install -e .`
5. Inicie o servidor: `uvicorn src.main:app --reload`
6. Acesse http://localhost:8000 para verificar o funcionamento