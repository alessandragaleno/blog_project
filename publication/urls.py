from django.contrib import admin, home
from django.urls import path
from .views import home  # noqa: F811

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
]
