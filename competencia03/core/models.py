from django.db import models
from django.contrib.auth.models import User

class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    criador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='empresas_criadas')
    membros = models.ManyToManyField(User, related_name='empresas_vinculadas', blank=True)

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='projetos')
    criador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projetos_criados')
    membros = models.ManyToManyField(User, related_name='projetos_participantes', blank=True)

    def __str__(self):
        return f"{self.nome} ({self.empresa.nome})"
