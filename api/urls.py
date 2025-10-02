from django.urls import path
from . import views

urlpatterns = [
    path("mapa/", views.mapa, name="mapa"),
    path("api/localizacao/", views.receber_localizacao, name="receber_localizacao"),
]
