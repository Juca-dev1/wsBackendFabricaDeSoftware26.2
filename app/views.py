from django.shortcuts import render
import requests

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from drf_spectacular.utils import extend_schema

@extend_schema(
    summary="Busca jogos externos",
    description="Retorna uma lista de jogos disponíveis em uma API externa."
)


@api_view(['GET'])
def buscar_jogos_externos(request):

    url = 'https://www.freetogame.com/api/games'

    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        jogos_externos = resposta.json()
        return Response(jogos_externos, status=status.HTTP_200_OK)


    except requests.RequestException:
        
        return Response(
            {'erro': 'Erro ao buscar jogos externos'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from drf_spectacular.utils import extend_schema, OpenApiResponse
from .serializers import TokenRequestSerializer, TokenResponseSerializer


class CustomObtainAuthToken(ObtainAuthToken):

    @extend_schema(
        request=TokenRequestSerializer,
        responses=
        {200: TokenResponseSerializer}
    )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )

        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']

        token, created = Token.objects.get_or_create(
            user=user
        )

        return Response(
            {'token': token.key}
        )
def home(request):
        return render(
        request,
        'app/index.html'
    )