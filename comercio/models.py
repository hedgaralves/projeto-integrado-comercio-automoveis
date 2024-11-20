from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

class Automovel(models.Model):
    STATUS_CHOICES = [
        ('disponivel', 'Disponível'),
        ('vendido', 'Vendido'),
    ]
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='disponivel')

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano})"

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    automovel = models.ForeignKey(Automovel, on_delete=models.CASCADE)
    data_venda = models.DateField(auto_now_add=True)
    valor_final = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Venda: {self.automovel} para {self.cliente}"
