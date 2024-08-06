from django.urls import path
from .views import inicio, home, index

urlpatterns = [
    # arquivos html
    path('inicio/', inicio, name='inicio'),
    path('home/', home, name='home'),
    path('index/',index, name='index'),
]