from django.db import models

class DevelopmentModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class ProductionModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class PruebaProduccion(models.Model):
    name = models.CharField(max_length=100)  # Nombre del producto
    description = models.TextField(blank=True)  # Descripción del producto
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Precio
    stock = models.PositiveIntegerField(default=0)  # Cantidad en stock
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    updated_at = models.DateTimeField(auto_now=True)  # Fecha de actualización

    def __str__(self):
        return self.name
