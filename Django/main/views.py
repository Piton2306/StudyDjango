from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<button><u><h1>Приверка работы<h1><u><button>"
                        )


def about(request):
    return HttpResponse("<Страница про нас>")

