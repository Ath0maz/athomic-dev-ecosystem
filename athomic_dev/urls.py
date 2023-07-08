from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('servicos/', include('servicos.urls')),
    path('conteudo/', include('conteudo.urls')),
]
