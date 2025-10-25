from django.db import models
from datetime import datetime
from .consts import *

class Imoveis(models.Model):
    titulo = models.CharField(max_length=100)
    tipo = models.SmallIntegerField(choices=TIPO_IMOVEL_CHOICES)
    preco = models.DecimalField(max_digits=12, decimal_places=2)
    endereco = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    quartos = models.IntegerField(null=True, blank=True)
    banheiros = models.IntegerField(null=True, blank=True)
    area = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    data_publicacao = models.DateTimeField(default=datetime.now)
    cep = models.CharField(max_length=20,blank=True, null=True)
    imagem = models.ImageField(upload_to='imoveis/', null=True, blank=True)
    def __str__(self):
        return self.titulo
    
    @property
    def imovel_novo(self):
        return self.data_publicacao == datetime.now().year
    
    class Meta:
        ordering = ['-id']
