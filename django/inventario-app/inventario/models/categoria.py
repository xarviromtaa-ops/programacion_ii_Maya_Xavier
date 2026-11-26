from django.db import models
from django.urls import reverse


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    codigo_pasillo = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True, null=True)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('categoria_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ['nombre']
