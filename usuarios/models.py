from django.db import models


#Login: thiago@teste.com
#senha: thiago123


#adm
#login: thg
#senha: 1234

class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    senha = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.nome