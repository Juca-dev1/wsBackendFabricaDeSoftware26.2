from django.shortcuts import render
import requests

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET'])
def buscar_jogos_externos(request):

    url = 'https://www.freetogame.com/api/games'

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        jogos_externos = resposta.json()
        return Response(jogos_externos, status=status.HTTP_200_OK)


    except requests.RequestException:
        
        return Response(
            {'erro': 'Erro ao buscar jogos externos'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
