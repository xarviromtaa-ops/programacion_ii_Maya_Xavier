from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from .producto import Producto


class Movimiento(models.Model):
    class TipoMovimiento(models.TextChoices):
        ENTRADA = 'ENTRADA', 'Entrada de stock'
        SALIDA = 'SALIDA', 'Salida de stock'
        AJUSTE = 'AJUSTE', 'Ajuste de inventario'

    producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        related_name='movimientos',
    )
    tipo = models.CharField(
        max_length=15,
        choices=TipoMovimiento.choices,
        default=TipoMovimiento.ENTRADA,
    )
    cantidad = models.PositiveIntegerField()
    costo_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_movimiento = models.DateField()
    motivo = models.CharField(max_length=200)
    creado_por = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='movimientos_creados',
    )

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.producto.nombre} ({self.cantidad})"

    def get_absolute_url(self):
        return reverse('movimiento_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Movimiento"
        verbose_name_plural = "Movimientos"
        ordering = ['-fecha_movimiento', '-id']
