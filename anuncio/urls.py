from django.urls import path
from anuncio.views import *

urlpatterns = [
    path('', ListarAnuncios.as_view(), name='listar-anuncios'),
    path('novo/', CriarAnuncio.as_view(), name='criar-anuncio'),
    path('<int:pk>/', EditarAnuncio.as_view(), name='editar-anuncio'),
    path('deletar/<int:pk>/', DeletarAnuncio.as_view(), name='deletar-anuncio'),
]