from django.urls import path
from inventario.views.movimiento_views import (
    movimiento_create,
    movimiento_delete,
    movimiento_detail,
    movimiento_list,
    movimiento_update,
)

urlpatterns = [
    path(
        'movimientos/',
        movimiento_list,
        name='movimiento_list',
    ),
    path(
        'movimientos/<int:pk>/',
        movimiento_detail,
        name='movimiento_detail',
    ),
    path(
        'movimientos/crear/',
        movimiento_create,
        name='movimiento_create',
    ),
    path(
        'movimientos/<int:pk>/editar/',
        movimiento_update,
        name='movimiento_update',
    ),
    path(
        'movimientos/<int:pk>/eliminar/',
        movimiento_delete,
        name='movimiento_delete',
    ),
]
