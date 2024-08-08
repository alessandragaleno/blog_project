from django.urls import path
from .views import inicio,  list, delete

urlpatterns = [
    # arquivos html
    path('inicio/', inicio, name='inicio'),
    path('list/', list, name='listar_author'),
    path('delete/', delete, name='author_confirm_delete')
]