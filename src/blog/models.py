from django.db import models
from django.utils import timezone


# Create your models here.
class Postagem(models.Model):
    titulo = models.CharField(max_length=20)
    texto = models.TextField()

    criado_em = models.DateTimeField(default=timezone.now)
    publicado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
