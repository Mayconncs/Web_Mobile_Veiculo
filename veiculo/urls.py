from django.urls import path
from veiculo.views import *
from veiculo.views import APIListarVeiculos

urlpatterns= [
    path('', ListarVeiculos.as_view(), name='listar-veiculos'),
    path('novo/', CriarVeiculos.as_view(), name='criar-veiculos'),
    path('<int:pk>/', EditarVeiculos.as_view(), name='editar-veiculos'),
    path('deletar/<int:pk>/', DeletarVeiculos.as_view(), name='deletar-veiculos'),
    path('api/', APIListarVeiculos.as_view(), name='api-listar-veiculos'),
    path('fotos/<str:arquivo>/', FotoVeiculo.as_view(), name='foto-veiculos')
]