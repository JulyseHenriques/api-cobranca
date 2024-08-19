# API de Cobranças

## Configuração

1. Clone o repositório:
    ```sh
    git clone <URL do repositório>
    cd cobrancas_api
    ```

2. Construa e execute os contêineres Docker:
    ```sh
    docker-compose up --build
    ```

3. Acesse a API no endereço [http://localhost:8000](http://localhost:8000).

## Endpoints

### POST /upload-csv/

- **Descrição**: Processa um arquivo CSV com informações de débitos.
- **Arquivo CSV**: 

- **Resposta**: `{ "message": "CSV processed successfully" }`

### POST /generate-bills/

- **Descrição**: Gera boletos e envia e-mails para os contatos.
- **Resposta**: `{ "message": "Bills generated and sent" }`

## Testes

1. Execute os testes:
  ```sh
  pytest
  ```
