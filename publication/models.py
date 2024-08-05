from django.db import models

# Create your models here.
class Publication(models.Model):
    author = models.ForeignKey('author.Author', on_delete=models.CASCADE, verbose_name='publication')  # noqa: F821
    date_pubication = models.DateTimeField('publication date', auto_now_add=True)
    pub_text = models.TextField('publications', max_length=255)
    pub_title = models.CharField('publication title', max_length=200)

    class Meta:
        db_table = 'publications'