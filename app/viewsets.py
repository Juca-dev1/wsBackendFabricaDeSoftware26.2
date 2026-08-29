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

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class DesenvolvedoraViewSet(viewsets.ModelViewSet):
    queryset = Desenvolvedora.objects.all()
    serializer_class = DesenvolvedoraSerializer

class JogoViewSet(viewsets.ModelViewSet):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
