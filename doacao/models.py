from django.db import models
from estoque.models import Item

class Doacao(models.Model):
    CATEGORIAS = [
        ('AL', 'Alimentos'),
        ('HG', 'Higiene'),
        ('LM', 'Limpeza'),
        ('VD', 'Vestuário'),
        ('OT', 'Outros'),
    ]
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    unidade_medida = models.CharField(max_length=20)
    categoria = models.CharField(max_length=2, choices=CATEGORIAS)
    doador = models.CharField(max_length=100)
    data_doacao = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        item, created = Item.objects.get_or_create(
            nome=self.nome,
            defaults={
                "quantidade": 0,
                "unidade_medida": self.unidade_medida,
                "categoria": self.categoria,
            }
        )

        item.registrar_entrada(self.quantidade)

    def __str__(self):
        return f"{self.nome} - {self.quantidade} {self.unidade_medida}"
