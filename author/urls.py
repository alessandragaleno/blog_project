from django.urls import path
from .views import inicio,home, index, contact, post

urlpatterns = [
    # arquivos html
    path('inicio/', inicio, name='inicio'),
    path('home/', home, name='home'),
    path('index/',index, name='index'),
    path('contact/', contact, name='contact'),
    path('post/', post, name='post'),
]
]