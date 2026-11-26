from django.urls import path
from inventario.views.producto_views import (
    producto_create,
    producto_delete,
    producto_detail,
    producto_list,
    producto_update,
)

urlpatterns = [
    path(
        'productos/',
        producto_list,
        name='producto_list',
    ),
    path(
        'productos/<int:pk>/',
        producto_detail,
        name='producto_detail',
    ),
    path(
        'productos/crear/',
        producto_create,
        name='producto_create',
    ),
    path(
        'productos/<int:pk>/editar/',
        producto_update,
        name='producto_update',
    ),
    path(
        'productos/<int:pk>/eliminar/',
        producto_delete,
        name='producto_delete',
    ),
]
