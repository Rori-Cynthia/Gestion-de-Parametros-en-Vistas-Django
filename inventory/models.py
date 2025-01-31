from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Nombre'
    )
    country = models.CharField(
        max_length=100,
        verbose_name='País'
    )

    class Meta:
        verbose_name = 'Manufacturer'
        verbose_name_plural = 'Manufacturers'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Nombre'
    )
    description = models.TextField(
        verbose_name='Descripción'
    )
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        verbose_name='Precio'
    )
    expiration_date = models.DateField(
        null=True, 
        blank=True, 
        verbose_name='Fecha de vencimiento'
    )
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Fabricante'
    )

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f"{self.name} ({self.manufacturer})"
