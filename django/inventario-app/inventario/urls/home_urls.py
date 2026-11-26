from django.urls import path
from inventario.views.home_views import home_view

urlpatterns = [
    path('', home_view, name='home'),
]
