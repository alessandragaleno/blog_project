# blog/views.py
from django.shortcuts import render
from .models import Author

def author_list(request):
    authors = Author.objects.all()  # noqa: F841
    return render(request, 'blog/author_list.html', {'name': name})
