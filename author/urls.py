from django.urls import path
from . import views

urlpatterns = [
    # arquivos html
    path('login/', views.login_user, name='login'),
    path('cadastro/', views.register_user, name='cadastro')
]
