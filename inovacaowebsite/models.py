from django.db import models
import datetime

class Noticia(models.Model):
    imagem = models.ImageField(upload_to='noticias')
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    conteudo = models.TextField()
    autor = models.CharField(max_length=100, default='Inovação JFPB')
    slug = models.SlugField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Notícia"
        ordering = ['-data']

    def __str__(self):
        return self.titulo

class Equipe(models.Model):
    imagem = models.ImageField(upload_to='equipe')
    nome = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    funcao = models.CharField(max_length=100)
    descricao = models.TextField()
    twitter = models.URLField(max_length=200, blank=True)
    facebook = models.URLField(max_length=200, blank=True)
    instagram = models.URLField(max_length=200, blank=True)
    linkedin = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.nome
    
class Parceiro(models.Model):
    imagem = models.ImageField(upload_to='parceiros')
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.nome
    
# Galeria de imagens

class Album(models.Model):
    capa = models.ImageField(upload_to='galeria')
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Albuns"
        ordering = ['-data']

    def __str__(self):
        return self.titulo
    
class Imagem(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='galeria')
    descricao = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Imagens"
        ordering = ['-data']

    def __str__(self):
        return self.descricao
    
# Contato
class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    assunto = models.CharField(max_length=100)
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data']

    def __str__(self):
        return self.nome + ' - ' + self.assunto

class Projeto(models.Model):
    status_choices = (('Pendência', 'Pendência'), ('Em Andamento', 'Em Andamento'), ('Concluído', 'Concluído'))

    imagem = models.ImageField(upload_to='projetos')
    titulo = models.CharField(max_length=100)
    status = models.CharField(choices=status_choices, default='Pendência', max_length=24)
    descricao = models.TextField()
    conteudo = models.TextField()
    autor = models.CharField(max_length=100, default='Inovação JFPB')
    slug = models.SlugField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data']

    def __str__(self):
        return self.titulo
    
class Premio(models.Model):
    imagem = models.ImageField(upload_to='premios')
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    conteudo = models.TextField()
    autor = models.CharField(max_length=100, default='Inovação JFPB')
    slug = models.SlugField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data']

    def __str__(self):
        return self.titulo
    
class Tipo_De_Legislacao(models.Model):
    nome = models.CharField(unique=True, max_length=48)

    class Meta:
        verbose_name = "Tipo de Legislação"
        verbose_name_plural = "Tipos de Legislações"

    def __str__(self):
        return self.nome
    

    

class Legislacao(models.Model):
    tipo = models.ForeignKey(Tipo_De_Legislacao, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()

    class Meta:
        verbose_name = "Legislação"
        verbose_name_plural = "Legislações"

    def __str__(self):
        return self.tipo.nome + " - " + self.titulo

class Legislacao_Informacoes(models.Model):
    categoria = models.ForeignKey(Legislacao, on_delete=models.CASCADE)
    url = models.URLField(max_length=200)
    nome = models.CharField(max_length=100)
    lei = models.CharField(max_length=100)
    ano = models.CharField(max_length=4)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Legislação Informação"
        verbose_name_plural = "Legislação Informações"
        ordering = ['-data']

    def __str__(self):
        return self.nome + " - " + self.categoria.titulo