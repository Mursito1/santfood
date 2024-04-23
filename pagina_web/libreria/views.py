from django.shortcuts import render # type: ignore


def index(request):
    return render (request, 'paginas/index.html')

def nosotros(request):
    return render (request, 'paginas/nosotros.html')


def menus (request):
    return render (request, 'paginas/menus.html')


def registro (request):
    return render (request, 'paginas/registro.html')