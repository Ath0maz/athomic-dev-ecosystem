from django.urls import path
from . import views

urlpatterns = [
    path('conteudo_page/', views.conteudo_page, name="conteudo_page"),
    
]