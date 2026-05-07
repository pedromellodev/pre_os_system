from django.db import models
from django.contrib.auth.models import User

class Orcamento(models.Model):
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('PRONTO', 'Pronto para envio'),
        ('EM CURSO', 'Em curso'),
    ]

    TIPO_USO_CHOICES = [
        ('RESIDENCIAL', 'Residencial'),
        ('COMERCIAL', 'Comercial'),
    ]

    nome_cliente = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=15)

    logradouro = models.CharField(max_length=255)
    municipio_codigo = models.IntegerField()

    os_vistoria = models.CharField(max_length=50)

    site = models.IntegerField()
    economias = models.IntegerField()

    tipo_uso = models.CharField(max_length=20, choices=TIPO_USO_CHOICES)

    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDENTE')

    criado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome_cliente} - {self.os_vistoria} - {self.status}'