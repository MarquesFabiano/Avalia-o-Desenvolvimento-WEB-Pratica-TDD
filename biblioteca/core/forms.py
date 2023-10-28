from django import forms
from django.core.exceptions import ValidationError
from core.models import LivroModel


def validate_title(value):
    if len(value) < 10:
        raise ValidationError('Deve ter pelo menos dez caracteres')

def validate_ano(ano):
    if not ano.isdigit():
        raise ValidationError('O ano deve conter apenas dígitos.')

    if len(ano) != 4:
        raise ValidationError('O ano deve ter exatamente 4 dígitos.')

class LivroForm(forms.ModelForm):

    class Meta:
        model = LivroModel
        fields = ['titulo', 'editora','autor', 'ano']
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
            }
        }

    def clean_titulo(self):
        titulo = self.cleaned_data['titulo']
        validate_title(titulo)
        return titulo

    def clean_editora(self):
        editora = self.cleaned_data['editora']
        validate_title(editora)
        return editora

    def clean_autor(self):
        autor =self.cleaned_data['autor']
        validate_title(autor)
        return autor
    
    def clean_ano(self):
        ano =self.cleaned_data['ano']
        validate_title(ano)
        return ano    

    def clean(self):
        self.cleaned_data = super().clean()
        return self.cleaned_data

