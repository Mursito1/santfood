from django.urls import path
from .views import index, nosotros, menus, registro


urlpatterns = [
    path('', index, name = 'index'),
    path('nosotros', nosotros, name = 'nosotros'),
    path('menus', menus, name = 'menus'),
    path('registro', registro , name = 'registro')
]