from django.shortcuts import render
from .models import Localizacao


def mapa(request):
    # Pegamos a última localização salva
    ultima = Localizacao.objects.last()
    return render(request, "mapa.html", {"ultima": ultima})
