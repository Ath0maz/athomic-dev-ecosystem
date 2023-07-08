from django.shortcuts import render
from django.http import HttpResponse

def conteudo_page(request):
    return HttpResponse('estou em conteudo')
