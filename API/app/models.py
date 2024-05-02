from django.db import models
from uuid import uuid4

class Cadastro(models.Model):
    nome = models.CharField(max_length=250)
    idade = models.IntegerField()
    email = models.EmailField(default='exemple@exemplo.com')
    data_cadastro = models.DateField(auto_now_add=True)
