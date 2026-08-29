from rest_framework import serializers

from .models import (
    Genero,
    Desenvolvedora,
    Jogo,
    Usuario,
)

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'

    def validate_nome(self, value):
         if not value.strip():
            raise serializers.ValidationError(
                'O nome não pode ficar vazio.'
            )

         return value

class DesenvolvedoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desenvolvedora
        fields = '__all__'

    def validate_nome(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                'O nome não pode ficar vazio.'
            )

        return value

class JogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogo
        fields = '__all__'

    def validate_nota(self, value):
        if value < 0 or value > 10:
            raise serializers.ValidationError(
                'A nota deve estar entre 0 e 10.'
            )

        return value

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

    def validate_nome(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                'O nome não pode ficar vazio.'
            )

        return value
    
class TokenRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class TokenResponseSerializer(serializers.Serializer):
    token = serializers.CharField()