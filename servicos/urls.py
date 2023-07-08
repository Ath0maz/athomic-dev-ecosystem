from django.urls import path
from . import views

urlpatterns = [
    path('servicos_page/', views.servicos_page, name="servicos_page"),
    
]