from django.shortcuts import render
from django.http import HttpResponse

def servicos_page(request):
    return HttpResponse('estou em servicos')