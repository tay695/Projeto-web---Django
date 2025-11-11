from django.db import models

# cadastros/models.py
from django.db import models

class Doador(models.Model):
    TIPO_CHOICES = [
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica'),
    ]
    nome = models.CharField(max_length=200, verbose_name="Nome/Razão Social")
    tipo = models.CharField(max_length=2, choices=TIPO_CHOICES, default='PF')
    documento = models.CharField(max_length=20, unique=True, blank=True, null=True, verbose_name="CPF/CNPJ")
    contato = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Doador"
        verbose_name_plural = "Doadores"

class EntidadeBeneficiada(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    responsavel = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    num_beneficiados = models.PositiveIntegerField(default=0, verbose_name="Pessoas Atendidas")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Entidade Beneficiada"
        verbose_name_plural = "Entidades Beneficiadas"
