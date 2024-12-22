from django import forms
from .models import Author
from django.contrib.auth.forms import UserCreationForm  # noqa: F401

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)

    class Meta:
        model = Author
        fields = ('username', 'email', 'password1', 'password2')


class LogoutForm(forms.Form):
    username = forms.CharField(max_length=255, required=False)
    password = forms.CharField(required=False, widget=forms.PasswordInput)

    class Meta:
        model = Author
        fields = ('username', 'email', 'password1', 'password2')

