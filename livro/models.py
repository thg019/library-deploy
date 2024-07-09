from django.db import models
from datetime import date
import datetime
from usuarios.models import Usuario


class Categoria(models.Model):
    nome = models.CharField(max_length=40)
    descricao = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    

    def __str__(self) -> str:
        return self.nome
    

class Livros(models.Model):
    img = models.ImageField(upload_to='capa_livro', null=True, blank=True)
    nome = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    co_autor = models.CharField(max_length=50, blank=True)
    data_de_cadastro = models.DateField(default=date.today)
    emprestado = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Livro'

    def __str__(self):
        return self.nome


#Emprestimos se estivesse acima da classe Livros daria erro pois ela 'não existiria' ainda, tem que colocar após a classe Livros.
class Emprestimos(models.Model):
    choices = (
        ('P', 'Péssimo'),
        ('R', 'Ruim'),
        ('B', 'Bom'),
        ('O', 'Ótimo'),
    )
    nome_emprestado = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, blank=True, null=True)
    nome_emprestado_anonimo = models.CharField(max_length=50, blank=True, null=True)
    data_emprestimo = models.DateTimeField(default=datetime.datetime.now())
    data_devolucao = models.DateTimeField(blank=True, null=True)
    livro = models.ForeignKey(Livros, on_delete=models.DO_NOTHING)
    avaliacao = models.CharField(max_length=1, choices=choices, null=True, blank=True)

    class Meta:
        verbose_name = 'Emprestimo'

    def __str__(self):
        return f"{self.nome_emprestado} | {self.livro}"
