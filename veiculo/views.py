from django.http import FileResponse, Http404
from django.urls import reverse_lazy
from django.views import View
from veiculo.models import Veiculo
from django.views.generic import ListView, CreateView
from veiculo.forms import FormularioVeiculo
from django.core.exceptions import ObjectDoesNotExist

class ListarVeiculos(ListView):
    model = Veiculo
    context_object_name = 'veiculos'
    template_name = 'veiculo/listar.html'

class CriarVeiculos(CreateView):
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/novo.html'
    success_url = reverse_lazy('listar-veiculos')

class FotoVeiculo(View):
    def get(self, request, arquivo):
        try:
            veiculo = Veiculo.objects.get(foto='veiculo/fotos/()'.format(arquivo))
            return FileResponse(veiculo.foto)
        except ObjectDoesNotExist:
            raise Http404("Foto não encontrada ou acesso não autorizado")
        except Exception as exception:
            raise exception
            