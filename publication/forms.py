from django import forms

from .models import Publication

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ('pub_title', 'pub_text')
        widget = {
            'pub_title': forms.TextInput(attrs={'arrow' : 10, 'cols': 50})
        }


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
