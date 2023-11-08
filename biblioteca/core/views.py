from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .forms import LivroForm
from .models import LivroModel
import requests

def get_book_cover(book_title):
    base_url = "https://openlibrary.org/api/books"
    params = {
        "bibkeys": f"ISBN:{book_title}",
        "format": "json",
        "jscmd": "data"
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        if f"ISBN:{book_title}" in data:
            cover_url = data[f"ISBN:{book_title}"]["cover"]["large"]
            return cover_url

    return None

def index(request):
    if request.method == 'GET':
        return render(request, "index.html")
    else:
        return HttpResponseRedirect(reverse('core:index'))

def cadastro(request):
    if request.method == 'POST':
        form_livro = LivroForm(request.POST)
        if form_livro.is_valid():
            eleitor = LivroModel.objects.create(**form_livro.cleaned_data)
            return HttpResponseRedirect(reverse('core:index'))
        else:
            contexto = {'formulario_livro': form_livro}
            return render(request, "cadastro.html", contexto)
    else:
        contexto = {'formulario_livro': LivroForm()}
        return render(request, 'cadastro.html', contexto)

def listar(request):
    if request.method == 'POST':
        livro_id = request.POST.get('livro_id', '')
        try:
            livro = LivroModel.objects.get(pk=livro_id)
            
            book_title = livro.isbn
            cover_url = get_book_cover(book_title)
            
            contexto = {'livro': livro, 'cover_url': cover_url}
        except ValueError:
            contexto = {}
        return render(request, "detalhes.html", contexto)
    else:
        livros = LivroModel.objects.all()
        contexto = {'livros': livros}
        return render(request, 'listar.html', contexto)
