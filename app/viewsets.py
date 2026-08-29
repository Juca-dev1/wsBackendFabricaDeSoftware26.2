from rest_framework import viewsets

from .models import (
    Genero,
    Desenvolvedora,
    Jogo,
    Usuario,
)

from .serializers import (
    GeneroSerializer,
    DesenvolvedoraSerializer,
    JogoSerializer,
    UsuarioSerializer,
)

from drf_spectacular.utils import extend_schema_view, extend_schema


@extend_schema_view(
    list=extend_schema(
        summary="Lista todos os gêneros",
        description="Retorna todos os gêneros cadastrados."
    ),
    retrieve=extend_schema(
        summary="Consulta um gênero",
        description="Retorna os dados de um gênero específico."
    ),
    create=extend_schema(
        summary="Cadastra um gênero",
        description="Cria um novo gênero."
    ),
    update=extend_schema(
        summary="Atualiza um gênero",
        description="Atualiza completamente um gênero."
    ),
    partial_update=extend_schema(
        summary="Atualiza parcialmente um gênero",
        description="Atualiza parcialmente os dados de um gênero."
    ),
    destroy=extend_schema(
        summary="Exclui um gênero",
        description="Remove um gênero do sistema."
    ),
)
class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer


@extend_schema_view(
    list=extend_schema(
        summary="Lista todas as desenvolvedoras",
        description="Retorna todas as desenvolvedoras cadastradas."
    ),
    retrieve=extend_schema(
        summary="Consulta uma desenvolvedora",
        description="Retorna os dados de uma desenvolvedora específica."
    ),
    create=extend_schema(
        summary="Cadastra uma desenvolvedora",
        description="Cria uma nova desenvolvedora."
    ),
    update=extend_schema(
        summary="Atualiza uma desenvolvedora",
        description="Atualiza completamente uma desenvolvedora."
    ),
    partial_update=extend_schema(
        summary="Atualiza parcialmente uma desenvolvedora",
        description="Atualiza parcialmente os dados de uma desenvolvedora."
    ),
    destroy=extend_schema(
        summary="Exclui uma desenvolvedora",
        description="Remove uma desenvolvedora do sistema."
    ),
)
class DesenvolvedoraViewSet(viewsets.ModelViewSet):
    queryset = Desenvolvedora.objects.all()
    serializer_class = DesenvolvedoraSerializer


@extend_schema_view(
    list=extend_schema(
        summary="Lista todos os jogos",
        description="Retorna uma lista com todos os jogos cadastrados."
    ),
    retrieve=extend_schema(
        summary="Consulta um jogo",
        description="Retorna os dados de um jogo específico."
    ),
    create=extend_schema(
        summary="Cadastra um jogo",
        description="Cria um novo jogo no sistema."
    ),
    update=extend_schema(
        summary="Atualiza um jogo",
        description="Atualiza completamente os dados de um jogo."
    ),
    partial_update=extend_schema(
        summary="Atualiza parcialmente um jogo",
        description="Atualiza parcialmente os dados de um jogo."
    ),
    destroy=extend_schema(
        summary="Exclui um jogo",
        description="Remove um jogo do sistema."
    ),
)
class JogoViewSet(viewsets.ModelViewSet):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer


@extend_schema_view(
    list=extend_schema(
        summary="Lista todos os usuários",
        description="Retorna todos os usuários cadastrados."
    ),
    retrieve=extend_schema(
        summary="Consulta um usuário",
        description="Retorna os dados de um usuário específico."
    ),
    create=extend_schema(
        summary="Cadastra um usuário",
        description="Cria um novo usuário."
    ),
    update=extend_schema(
        summary="Atualiza um usuário",
        description="Atualiza completamente um usuário."
    ),
    partial_update=extend_schema(
        summary="Atualiza parcialmente um usuário",
        description="Atualiza parcialmente os dados de um usuário."
    ),
    destroy=extend_schema(
        summary="Exclui um usuário",
        description="Remove um usuário do sistema."
    ),
)
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer 