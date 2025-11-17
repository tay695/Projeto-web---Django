from django.db import models

STATUS_CHOICES = [('PENDENTE', 'Pendente'),
                ('APROVADA', 'Aprovada'),
                ('CANCELADA', 'Cancelada'),

]
class Doacao(models.Model):
    
    doador = models.ForeignKey('doador.Doador', on_delete=models.CASCADE)
    estoque = models.ForeignKey('estoque.Item', on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    data_doacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField (
        max_length=10,
        choices=STATUS_CHOICES,
        default='PENDENTE')
    
    
def __str__(self):
    return f"{self.quantidade} - {self.doador.nome} - {self.data_doacao} - {self.status}"

