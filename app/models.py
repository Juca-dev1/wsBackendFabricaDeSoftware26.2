from django.db import models

class Genero(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

class Desenvolvedora(models.Model):
    nome = models.CharField(max_length=150)
    pais = models.CharField(max_length=100)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.nome

class Jogo(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)
    data_lancamento = models.DateField()
    nota = models.DecimalField(
        max_digits=3,
        decimal_places=1
    )

    genero = models.ForeignKey(
        Genero,
        on_delete=models.CASCADE,
        related_name='jogos'
    )

    desenvolvedora = models.ForeignKey(
        Desenvolvedora,
        on_delete=models.CASCADE,
        related_name='jogos'
    )

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome