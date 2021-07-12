from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


from .views import *


urlpatterns = [
  path('',  list_ramos, name='list_ramos'),
  path('validar/',  validar_usuario, name='Validar'),
  path('horario/',  horario, name='horario'),
]
