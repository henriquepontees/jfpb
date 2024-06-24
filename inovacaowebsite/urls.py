from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [path('', home, name='home'),
               path('galeria', galeria, name='galeria'),
               path('galeria/album/<int:album_id>', album, name='album'),
               path('contato', contato, name='contato'),
               path('noticias', noticias, name='noticias'),
               path('noticias/<int:noticia_id>', noticia, name='noticia'),
               path('premios', premios, name='premios'),
               path('premios/<int:premio_id>', premio, name='premio'),
               path('projetos', projetos, name='projetos'),
               path('projetos/<int:projeto_id>', projeto, name='projeto'),
               path('legislacoes', legislacoes, name='legislacoes'),
               path('legislacoes/<int:legi_id>', legislacao, name='legislacao'),
               path('sobre', sobre, name='sobre')]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)