# API de Gerenciamento de Usuários com Flask

## 📝 Descrição do Projeto

Este projeto é uma API RESTful simples para gerenciamento de usuários, desenvolvida como uma atividade acadêmica. A aplicação foi construída utilizando Python e o micro-framework Flask. Ela permite realizar as quatro operações básicas de um CRUD (Create, Read, Update, Delete) sobre uma lista de usuários mantida em memória, simulando um banco de dados.

## ✨ Funcionalidades

A API expõe os seguintes endpoints para manipulação de recursos de usuários:

| Método | Rota               | Descrição                              | Corpo da Requisição (JSON)             | Resposta de Sucesso          |
|--------|--------------------|----------------------------------------|----------------------------------------|------------------------------|
| `POST` | `/users`           | Cria um novo usuário.                  | `{ "nome": "string", "email": "string" }` | `201 Created` + usuário criado |
| `GET`  | `/users/<id>`      | Busca um usuário pelo seu ID.          | N/A                                    | `200 OK` + dados do usuário    |
| `PUT`  | `/users/<id>`      | Atualiza um usuário existente.         | `{ "nome": "string", "email": "string" }` | `200 OK` + usuário atualizado  |
| `DELETE`| `/users/<id>`     | Deleta um usuário pelo seu ID.         | N/A                                    | `200 OK` + mensagem de sucesso |

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Flask**

## 🚀 Como Executar o Projeto

Siga os passos abaixo para executar a aplicação localmente:

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git](https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git)
   ```

2. **Navegue até o diretório do projeto:**
   ```bash
   cd nome-do-repositorio
   ```

3. **Crie e ative um ambiente virtual:**
   ```bash
   # Criar o ambiente
   python -m venv venv

   # Ativar no Windows
   .\venv\Scripts\activate

   # Ativar no macOS/Linux
   source venv/bin/activate
   ```

4. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Execute a aplicação:**
   ```bash
   python app.py
   ```

A API estará disponível em `http://127.0.0.1:5000`. Você pode usar ferramentas como o [Postman](https://www.postman.com/) para testar os endpoints.