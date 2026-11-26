from django.urls import path
from django.views.generic.base import RedirectView
from inventario.views.auth_views import login_view, logout_view, registro_view

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='login', permanent=False)),
    path('registro/', registro_view, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
