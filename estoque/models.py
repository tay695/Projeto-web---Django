from django.db import models

# Create your models here.
class Item(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    categoria = models.CharField(max_length=50)
    unidade_medida = models.CharField(max_length=20)


    def registrar_entrada(self, quantidade):
        if quantidade > 0:
            self.quantidade += quantidade
            self.save()
    
    def registrar_saida(self, quantidade):
        if quantidade > 0 and quantidade <= self.quantidade:
            self.quantidade -= quantidade
            self.save()
        else:
            print("Quantidade insuficiente em estoque.")

    def __str__(self):
        return f"{self.nome} - {self.quantidade} {self.unidade_medida} ({self.categoria})"
        