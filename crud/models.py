from django.db import models

class Cliente(models.Model):
    documento = models.CharField(max_length=18, unique=True)
    nome_razao = models.CharField(max_length=255)
    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    pais = models.CharField(max_length=100, default="Brasil")
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nome_razao} - {self.documento}"
