# blog/forms.py
from django import forms
from author.models import Author, Publication

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['pub_title', 'author', 'pub_text', 'date_pubication']
        widgets = {
            'author': forms.Select(choices=[(a.id, a.name) for a in Author.objects.all()])
        }

