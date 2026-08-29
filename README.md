# 🎮 Sistema de Jogos

API REST desenvolvida em Django e Django REST Framework para gerenciamento de jogos.


##  Sobre o projeto

O Sistema de Jogos é uma API REST desenvolvida com Python, Django e Django REST Framework.

O projeto permite realizar operações de cadastro, consulta, alteração e exclusão de informações relacionadas a usuários, jogos, gêneros e desenvolvedoras.

Além disso, o sistema realiza o consumo de uma API externa para obter informações sobre jogos.


## Tecnologias utilizadas

- Python
- Django
- Django REST Framework
- SQLite
- Requests
- drf-spectacular
- Sawgger

## Entidades

O sistema possui quatro entidades principais:

- Usuário
- Jogo
- Gênero
- Desenvolvedora

## Relacionamentos

Um jogo possui:

- Um gênero
- Uma desenvolvedora

As relações são implementadas utilizando chaves estrangeiras.

## Funcionalidades

- CRUD de usuários
- CRUD de jogos
- CRUD de gêneros
- CRUD de desenvolvedoras
- Consumo de API externa de jogos
- Tratamento de erros
- API REST
- Documentação da API
- Testes dos endpoints através do Swagger
- Consulta de jogos

## Rotas principais

### Usuários

`/api/usuarios/`

### Jogos

`/api/jogos/`

### Gêneros

`/api/generos/`

### Desenvolvedoras

`/api/desenvolvedoras/`

### Jogos externos

`/api/jogos-externos/`

## Como executar o projeto

### 1. Execute estes Códigos no terminal sequencialmente

```bash
git clone https://github.com/Juca-dev1/wsBackendFabricaDeSoftware26.2.git

cd wsBackendFabricaDeSoftware26.2

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
