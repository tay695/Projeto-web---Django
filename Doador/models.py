from django.db import models

nome = models.CharField(max_length=100)
email = models.EmailField(unique=True)
telefone = models.CharField(max_length=15, blank=True, null=True)
endereco = models.TextField(blank=True, null=True)
data_cadastro = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return "{self.nome} - {self.email} - {self.telefone} - {self.endereco} - {self.data_cadastro}"


