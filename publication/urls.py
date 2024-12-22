from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='inicio'),
    path('sobre/', views.about, name='sobre'),
    path('contato/', views.contact, name='contato'),
    path('post/<int:id>/', views.post, name='post'),
    path('adicionar/', views.adicionar_publication, name='adicionar_publication')
]
