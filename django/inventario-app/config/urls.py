from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cuentas/', include('inventario.urls.auth_urls')),
    path('', include('inventario.urls.home_urls')),
    path(
        'inventario/',
        RedirectView.as_view(pattern_name='home', permanent=False),
        name='inventario',
    ),
    path('inventario/', include('inventario.urls')),
]
