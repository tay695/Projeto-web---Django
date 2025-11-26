from django.db import models
class PontoColeta(models.Model):

    STATUS_CHOICES = [
        ('ATIVO', 'Ativo'),
        ('INATIVO', 'Inativo / Fechado'),
    ]

    nome = models.CharField(max_length=255, verbose_name="Nome do Local")
    endereco = models.CharField(max_length=255, verbose_name="Endereço Completo")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ATIVO')
   
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Ponto de Coleta"
        verbose_name_plural = "Pontos de Coleta"