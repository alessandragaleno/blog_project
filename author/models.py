from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)

class Meta:
    db_table = 'authors'
