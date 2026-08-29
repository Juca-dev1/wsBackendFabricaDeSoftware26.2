# 🎮 Sistema de Jogos

API REST desenvolvida em Django e Django REST Framework para gerenciamento de jogos.

## Tecnologias utilizadas

- Python
- Django
- Django REST Framework
- SQLite
- Requests
- drf-spectacular

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

