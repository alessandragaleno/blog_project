from django.shortcuts import redirect, render

from .forms import PublicationForm
from .models import Publication


# Create your views here.
def index(request):
    publications = Publication.objects.all()

    return render(request, 'index.html', {'publictions': publications})

def about(request):
    return render(request, '/about.html')

def contact(request):
    return render(request, 'contact.html')

def post(request, id):
    publications = Publication.objects.get(id=id)
    return render(request, 'post.html', {'publication': publications})

def adicionar_publication(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'adicionar_publication.html', {'form': form})
