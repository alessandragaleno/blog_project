from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Author(AbstractUser):
    name = models.CharField(max_length=50)

class Meta:
    db_table = 'authors'
