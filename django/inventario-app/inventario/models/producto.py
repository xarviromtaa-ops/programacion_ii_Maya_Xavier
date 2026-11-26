from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from .categoria import Categoria
from .proveedor import Proveedor


class Producto(models.Model):
    class EstadoProducto(models.TextChoices):
        DISPONIBLE = 'DISPONIBLE', 'Disponible'
        STOCK_BAJO = 'STOCK_BAJO', 'Stock bajo'
        AGOTADO = 'AGOTADO', 'Agotado'
        DESCONTINUADO = 'DESCONTINUADO', 'Descontinuado'

    codigo_sku = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True, null=True)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name='productos',
    )
    proveedores = models.ManyToManyField(
        Proveedor,
        related_name='productos',
    )
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    stock_actual = models.PositiveIntegerField(default=0)
    stock_minimo = models.PositiveIntegerField(default=5)
    estado = models.CharField(
        max_length=20,
        choices=EstadoProducto.choices,
        default=EstadoProducto.DISPONIBLE,
    )
    fecha_ingreso = models.DateField()
    creado_por = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='productos_creados',
    )

    def __str__(self):
        return f"{self.codigo_sku} - {self.nombre}"

    def get_absolute_url(self):
        return reverse('producto_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['nombre']
