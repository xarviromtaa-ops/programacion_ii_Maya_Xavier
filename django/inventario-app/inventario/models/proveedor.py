from django.db import models
from django.urls import reverse


class Proveedor(models.Model):
    nombre = models.CharField(max_length=120)
    ruc = models.CharField(max_length=13, unique=True)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    ciudad = models.CharField(max_length=80)
    fecha_registro = models.DateField()

    def __str__(self):
        return f"{self.nombre} ({self.ruc})"

    def get_absolute_url(self):
        return reverse('proveedor_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ['nombre']
