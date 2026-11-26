from django.urls import include, path

urlpatterns = [
    path('', include('inventario.urls.categoria_urls')),
    path('', include('inventario.urls.proveedor_urls')),
    path('', include('inventario.urls.producto_urls')),
    path('', include('inventario.urls.movimiento_urls')),
]
