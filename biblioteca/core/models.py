from django.db import models

class LivroModel(models.Model):
    titulo = models.CharField('Título', max_length=200)
    editora = models.CharField('editora', max_length=200)
    autor = models.CharField('Autor', max_length=200)
    ano = models.IntegerField('Ano de Publicação', null=True, blank=True)


    def __str__(self):
        return self.titulo