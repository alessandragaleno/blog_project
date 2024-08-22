
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .forms import LoginForm


def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2:
            messages.error(request, 'As senhas não coicidem!')
            return redirect('register.html')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Este nome de usuário já existe!')
            return render(request, 'register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Este e-mail já existe!')
            return render(request, 'register.html')

        user = User.objects.create_user(username, email, password)
        user.save()
        messages.success(request, 'Usuário criado com sucesso!')
        return redirect('/')
    return render(request, 'author/cadastro.html')

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Nome de usuário ou senha inválidas!')
    else:
        form = LoginForm(request)
    return render(request, 'author/login.html', {'form': form})


def logout(request):
    return render(request, 'author/logout.html')