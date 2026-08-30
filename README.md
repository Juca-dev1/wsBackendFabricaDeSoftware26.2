# 👾 Ludex

API REST desenvolvida com **Python, Django e Django REST Framework** para gerenciamento de jogos.

O Ludex permite cadastrar e gerenciar jogos, gêneros, desenvolvedoras e usuários, além de consumir dados de uma API externa de jogos.

---

## 📌 Sobre o projeto

O **Ludex** é uma aplicação web desenvolvida com Django que disponibiliza uma API REST para gerenciamento de informações relacionadas a jogos.

O sistema permite realizar operações de:

- Cadastro
- Consulta
- Atualização
- Exclusão

Essas operações estão disponíveis para jogos, gêneros, desenvolvedoras e usuários.

O projeto também possui autenticação por Token, documentação interativa da API utilizando Swagger, integração com a API externa FreeToGame e uma página inicial desenvolvida com HTML, CSS e Django Templates.

---

## 🎮 Interface Web

O projeto possui uma página inicial que apresenta os principais recursos disponíveis no sistema.

A interface foi desenvolvida utilizando **HTML5, CSS3 e Django Templates**, com layout responsivo e identidade visual inspirada em jogos de luta.

Para acessar a página inicial após iniciar o servidor:

```text
http://127.0.0.1:8000/
```

A interface permite acessar a documentação e os principais recursos da API.

---

## 🛠️ Tecnologias utilizadas

- Python
- Django
- Django REST Framework
- SQLite
- Requests
- drf-spectacular
- Swagger / OpenAPI
- HTML5
- CSS3
- Django Templates

---

## 📦 Entidades

O sistema possui quatro entidades principais:

### Jogo

Armazena informações sobre os jogos cadastrados, como nome, descrição, data de lançamento, nota, gênero e desenvolvedora.

### Gênero

Representa a categoria de um jogo.

Exemplos:

```text
Ação
RPG
Aventura
Estratégia
```

### Desenvolvedora

Armazena informações sobre as empresas responsáveis pelo desenvolvimento dos jogos.

### Usuário

Armazena os dados dos usuários cadastrados no sistema.

---

## 🔗 Relacionamentos

Cada **Jogo** possui relacionamento com:

```text
Jogo
 ├── Gênero
 └── Desenvolvedora
```

Esses relacionamentos são implementados utilizando `ForeignKey` no Django.

---

## ⚙️ Funcionalidades

O Ludex possui:

- CRUD de jogos
- CRUD de gêneros
- CRUD de desenvolvedoras
- CRUD de usuários
- Autenticação por Token
- Validação de dados
- Tratamento de erros
- Integração com API externa
- Documentação OpenAPI
- Swagger UI
- ReDoc
- Interface web responsiva
---

## 🌐 Endpoints

| Recurso | Endpoint |
|---|---|
| Jogos | `/api/jogos/` |
| Gêneros | `/api/generos/` |
| Desenvolvedoras | `/api/desenvolvedoras/` |
| Usuários | `/api/usuarios/` |
| Jogos externos | `/api/jogos-externos/` |
| Token | `/api/token/` |
| Schema OpenAPI | `/api/schema/` |
| Swagger | `/api/schema/swagger-ui/` |
| ReDoc | `/api/schema/redoc/` |
---

## 🔐 Autenticação

A API utiliza autenticação baseada em **Token** do Django REST Framework.

Para obter um token, envie uma requisição:

```text
POST /api/token/
```

Informando usuário e senha.

Exemplo:

```json
{
    "username": "seu_usuario",
    "password": "sua_senha"
}
```

A API retornará um token:

```json
{
    "token": "seu_token"
}
```

Nas requisições autenticadas, utilize:

```text
Authorization: Token seu_token
```
---

## 📚 Documentação da API

O projeto utiliza **drf-spectacular** para gerar a documentação OpenAPI.

### Swagger UI

Permite visualizar e testar os endpoints diretamente pelo navegador:

```text
http://127.0.0.1:8000/api/schema/swagger-ui/
```

### ReDoc

Outra forma de visualizar a documentação:

```text
http://127.0.0.1:8000/api/schema/redoc/
```

### OpenAPI Schema

```text
http://127.0.0.1:8000/api/schema/
```
---

## 🌍 API Externa

O Ludex possui integração com a **FreeToGame API** para consultar informações sobre jogos externos.

A consulta pode ser realizada através do endpoint:

```text
GET /api/jogos-externos/
```

A integração utiliza a biblioteca `requests`.

Também foi implementado tratamento de erros e limite de tempo para evitar que uma falha na API externa mantenha a aplicação aguardando indefinidamente.

---

## ✅ Validações

Algumas validações foram implementadas para garantir a integridade dos dados.

### Jogos

A nota deve estar entre:

```text
0 e 10
```

### Usuários

O nome não pode ser vazio e o e-mail deve ser único.

Quando os dados enviados são inválidos, a API retorna uma mensagem de erro adequada.

---

# 🚀 Como executar o projeto

## 1. Clone o repositório

```bash
git clone https://github.com/Juca-dev1/wsBackendFabricaDeSoftware26.2.git
```

Entre na pasta:

```bash
cd wsBackendFabricaDeSoftware26.2
```
---

## 2. Crie o ambiente virtual

```bash
python -m venv venv
```
---

## 3. Ative o ambiente virtual

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```
---

## 4. Instale as dependências

```bash
pip install -r requirements.txt
```
---

## 5. Execute as migrações

```bash
python manage.py migrate
```

Isso criará as tabelas necessárias no banco de dados.
---

## 6. Crie um usuário administrador

Para acessar o Django Admin e gerar credenciais para autenticação, crie um superusuário:

```bash
python manage.py createsuperuser
```
Informe os dados solicitados pelo Django.

---
## 7. Inicie o servidor

```bash
python manage.py runserver
```

Se tudo estiver correto, o servidor será iniciado em:

```text
http://127.0.0.1:8000/
```
---

## 🧪 Como testar a API

A forma mais simples de testar o projeto é utilizando o Swagger.

Primeiro inicie o servidor e acesse:

```text
http://127.0.0.1:8000/api/schema/swagger-ui/
```

Depois:

1. Gere um token através de `/api/token/`.
2. Copie o token retornado.
3. Utilize a opção de autorização do Swagger.
4. Informe o token.
5. Teste os endpoints disponíveis.

Você poderá testar operações `GET`, `POST`, `PUT`, `PATCH` e `DELETE`.
---

## 📂 Estrutura principal

```text
app/
├── migrations/
├── static/
│   └── app/
│       ├── css/
│       └── img/
├── templates/
│   └── app/
│       └── index.html
├── models.py
├── serializers.py
├── views.py
└── viewsets.py

projeto/
├── settings.py
└── urls.py

manage.py
requirements.txt
README.md
```
---

## 🔄 Operações CRUD

Os principais recursos utilizam as operações padrão de uma API REST:

| Método | Operação |
|---|---|
| `GET` | Consultar dados |
| `POST` | Cadastrar dados |
| `PUT` | Atualizar completamente |
| `PATCH` | Atualizar parcialmente |
| `DELETE` | Excluir dados |

---

## 💾 Banco de dados

O projeto utiliza **SQLite** como banco de dados.

O Django gerencia a estrutura do banco através das migrations.

Sempre que houver alterações nos modelos, podem ser utilizados:

```bash
python manage.py makemigrations
python manage.py migrate
```
---
## 👾 Ludex

Projeto desenvolvido com **Django REST Framework** para gerenciamento e consulta de jogos.