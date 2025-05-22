from django.db import models
from veiculo.models import Veiculo
from django.conf import settings

class Anuncio(models.Model):
    OPCOES_STATUS = (
        (1, 'Ativo'),
        (2, 'Inativo'),
        (3, 'Reservado'),
    )
    
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, related_name='anuncios')
    preco_diaria = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(max_length=500, blank=True)
    status = models.SmallIntegerField(choices=OPCOES_STATUS, default=1)
    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Anúncio'
        verbose_name_plural = 'Anúncios'

    def __str__(self):
        return f"{self.veiculo.get_marca_display()} {self.veiculo.modelo} - R${self.preco_diaria}/dia"