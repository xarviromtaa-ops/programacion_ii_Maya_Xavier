from django.urls import path
from inventario.views.proveedor_views import (
    proveedor_create,
    proveedor_delete,
    proveedor_detail,
    proveedor_list,
    proveedor_update,
)

urlpatterns = [
    path(
        'proveedores/',
        proveedor_list,
        name='proveedor_list',
    ),
    path(
        'proveedores/<int:pk>/',
        proveedor_detail,
        name='proveedor_detail',
    ),
    path(
        'proveedores/crear/',
        proveedor_create,
        name='proveedor_create',
    ),
    path(
        'proveedores/<int:pk>/editar/',
        proveedor_update,
        name='proveedor_update',
    ),
    path(
        'proveedores/<int:pk>/eliminar/',
        proveedor_delete,
        name='proveedor_delete',
    ),
]
