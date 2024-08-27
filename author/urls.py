from django.urls import path

from .views import login_user, logout_user , register_user

urlpatterns = [
    # arquivos html
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('cadastro/', register_user, name='cadastro'),
]
