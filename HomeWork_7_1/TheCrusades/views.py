from django.shortcuts import render

from .models import Crusade

# Create your views here.


def index(request):
    yurishlar = Crusade.objects.all()
    return render(request, 'HTML/index.html', context={'yurishlar': yurishlar})


def index2(request,pk):
    yurishlar = Crusade.objects.get(pk=pk)
    return render(request, 'HTML/hl_2.html', context={'yurishlar': yurishlar})







