from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('index/', views.contact, name='contact'),
    path('post/<int:id>/', views.post, name='post'),
    path('adicionar/publication', views.adicionar_publication, name='adicionar_publication')
]
