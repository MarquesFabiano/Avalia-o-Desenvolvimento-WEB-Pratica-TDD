from django import forms
from django.core.exceptions import ValidationError
from core.models import LivroModel


def validate_title(titulo):
    if len(titulo) < 3:
        raise ValidationError('O título ter pelo menos três caracteres')

def validate_editora(editora):
    if len(editora) < 3:
        raise ValidationError('A editora deve ter pelo menos três caracteres')

def validate_ano(ano):
    if not ano.isdigit():
        raise ValidationError('O ano deve conter apenas dígitos.')

    if len(ano) != 4:
        raise ValidationError('O ano deve ter exatamente 4 dígitos.')
    
def validate_isbn(isbn):
    if not isbn.isdigit():
        raise ValidationError('O ISBN deve conter apenas dígitos.')
    
    if len(isbn) != 13:
        raise ValidationError('O ISBN deve conter 13 dígitos.')
    
def validate_paginas(paginas):
    if not paginas.isdgit():
        raise ValidationError('O número de páginas deve conter apenas dígitos.')
    
    if len(paginas) > 3:
        raise ValidationError('O número de páginas deve conter no máximo três dígitos.')

def validate_autor(autor):
    if len(autor) < 10:
        raise ValidationError('O nome do autor deve ter no minimo dez digitos')

class LivroForm(forms.ModelForm):

    class Meta:
        model = LivroModel
        fields = ['titulo', 'editora','autor', 'ano', 'isbn', 'paginas']
        error_messages = {
            'titulo': {
                'required': ("Informe o título do livro."),
            },
            'editora': {
                'required': ("Informe a editora do livro."),
            },
            'autor': {
                'required': ('Informe o autor do livro.')
            },
            'ano': {
                'required' : ('Informe o ano do livro')
            },
            'isbn': {
                'required' : ('Informe o ISBN do livro')
            },
            'paginas': {
                'required' : ('Informe o número de páginas do livro')
            }
        }

    def clean_titulo(self):
        titulo = self.cleaned_data['titulo']
        validate_title(titulo)
        return titulo

    def clean_editora(self):
        editora = self.cleaned_data['editora']
        validate_editora(editora)
        return editora

    def clean_autor(self):
        autor =self.cleaned_data['autor']
        validate_autor(autor)
        return autor
    
    def clean_ano(self):
        ano =self.cleaned_data['ano']
        validate_ano(ano)
        return ano

    def clean_isbn(self):
        isbn = self.cleaned_data['isbn']
        validate_isbn(isbn)
        return isbn

    def clear_paginas(self):
        paginas =self.cleaned_data['paginas']
        validate_paginas(paginas)
        return paginas    

    def clean(self):
        self.cleaned_data = super().clean()
        return self.cleaned_data

