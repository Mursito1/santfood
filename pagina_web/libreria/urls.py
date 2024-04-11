from django.urls import path
from .views import inicio, nosotros, menus, registro


urlpatterns = [
    path('', inicio, name = 'inicio'),
    path('nosotros', nosotros, name = 'nosotros'),
    path('menus', menus, name = 'menus'),
    path('registro', registro , name = 'registro')
]