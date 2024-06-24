from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import *

def home(request):
  template = loader.get_template('pages/home/home.html')
  context = {
             'equipe': Equipe.objects.all(),
             'parcerias': Parceiro.objects.all(),
             'noticias': Noticia.objects.order_by('-data')[:4]
            }
  return HttpResponse(template.render(context, request))

# Galeria de fotos

def galeria(request):
  template = loader.get_template('pages/galeria/galeria.html')
  context = {'albuns': Album.objects.order_by('-data')}
  return HttpResponse(template.render(context, request))

def album(request, album_id):
  try:
    chosenAlbum = Album.objects.get(id=album_id)
    template = loader.get_template('pages/galeria/galeria2.html')
    context = {'imagens': Imagem.objects.filter(album=chosenAlbum).order_by('-data')}
    return HttpResponse(template.render(context, request))
  except Album.DoesNotExist:
    return redirect('home')

# Contato

def contato(request):
  if(request.method == 'POST'):
    contato = Contato(nome=request.POST['nome'], email=request.POST['email'], mensagem=request.POST['assunto'], assunto=request.POST['mensagem'])
    contato.save()
  template = loader.get_template('pages/contato/contato.html')
  return HttpResponse(template.render({}, request))

# Notícias

def noticias(request):
    all_noticias = Noticia.objects.order_by('-data')
    if(request.method == 'POST'):
        search = request.POST['search']
        all_noticias = Noticia.objects.filter(titulo__contains=search).order_by('-data') 
    paginator = Paginator(all_noticias, 5)  # Show 5 noticias per page.

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    current_page = page_obj.number

    context = {
        'noticias': page_obj,
        'previous_page': current_page - 1,
        'next_page': current_page + 1,
    }

    return render(request, 'pages/noticias/noticias.html', context)

def noticia(request, noticia_id):
  try:
    chosenNoticia = Noticia.objects.get(id=noticia_id)
    template = loader.get_template('pages/noticias/noticia.html')
    context = {'noticia': chosenNoticia,
               'noticias': Noticia.objects.order_by('-data')[:5]}
    return HttpResponse(template.render(context, request))
  except Noticia.DoesNotExist:
    return redirect('home')
  
def premios(request):
    all_premios = Premio.objects.order_by('-data')
    if(request.method == 'POST'):
        search = request.POST['search']
        all_premios = Premio.objects.filter(titulo__contains=search).order_by('-data') 
    paginator = Paginator(all_premios, 5)  # Show 5 noticias per page.

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    current_page = page_obj.number

    context = {
        'premios': page_obj,
        'previous_page': current_page - 1,
        'next_page': current_page + 1,
    }

    return render(request, 'pages/premios/premios.html', context)

def premio(request, premio_id):
  try:
    chosenPremio = Premio.objects.get(id=premio_id)
    template = loader.get_template('pages/premios/premios_especificos.html')
    context = {'premio': chosenPremio,
               'premios': Premio.objects.order_by('-data')[:5]}
    return HttpResponse(template.render(context, request))
  except Premio.DoesNotExist:
    return redirect('home')

  # Projetos

def projetos(request):
    all_projetos = Projeto.objects.order_by('-data')
    if(request.method == 'POST'):
        search = request.POST['search']
        all_projetos = Projeto.objects.filter(titulo__contains=search).order_by('-data') 
    paginator = Paginator(all_projetos, 5)  # Show 5 noticias per page.

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    current_page = page_obj.number

    context = {
        'projetos': page_obj,
        'previous_page': current_page - 1,
        'next_page': current_page + 1,
    }

    return render(request, 'pages/projetos/projetos.html', context)
  
def projeto(request, projeto_id):
  try:
    chosenPremio = Projeto.objects.get(id=projeto_id)
    template = loader.get_template('pages/projetos/projetos_especificos.html')
    context = {'projeto': chosenPremio,
               'projetos': Projeto.objects.order_by('-data')[:5]}
    return HttpResponse(template.render(context, request))
  except Projeto.DoesNotExist:
    return redirect('home')


def legislacoes(request):
  tipos = Tipo_De_Legislacao.objects.all()
  legis = Legislacao.objects.all()
  context = {'tipos': tipos,
             'legis': legis}
  template = loader.get_template('pages/legislacoes/legislacoes.html')
  return HttpResponse(template.render(context, request))
  
def legislacao(request, legi_id):
  legi = Legislacao.objects.get(id=legi_id)
  legis = Legislacao_Informacoes.objects.filter(categoria=legi)
  context = {'legi': legi, 
             'legis': legis}
  template = loader.get_template('pages/legislacoes/legislacao.html')
  return HttpResponse(template.render(context, request))

  
def sobre(request):
  template = loader.get_template('pages/sobre/sobre.html')
  context = {}
  return HttpResponse(template.render(context, request))