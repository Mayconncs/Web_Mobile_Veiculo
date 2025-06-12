from django.http import FileResponse, Http404
from django.urls import reverse_lazy
from django.views import View
from veiculo.models import Veiculo
from django.views.generic import ListView, CreateView
from veiculo.forms import FormularioVeiculo
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from veiculo.serializers import SerializadorVeiculo
from rest_framework import permissions
from rest_framework.generics import DestroyAPIView

class ListarVeiculos(LoginRequiredMixin, ListView):
    model = Veiculo
    context_object_name = 'veiculos'
    template_name = 'veiculo/listar.html'

class CriarVeiculos(LoginRequiredMixin, CreateView):
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/novo.html'
    success_url = reverse_lazy('listar-veiculos')

class FotoVeiculo(View):
    def get(self, request, arquivo):
        try:
            veiculo = Veiculo.objects.get(foto='veiculo/fotos/{}'.format(arquivo))
            return FileResponse(veiculo.foto)
        except ObjectDoesNotExist:
            raise Http404("Foto não encontrada ou acesso não autorizado")
        except Exception as exception:
            raise exception
        
class EditarVeiculos(LoginRequiredMixin, UpdateView):
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/editar.html'
    success_url = reverse_lazy('listar-veiculos')

class DeletarVeiculos(LoginRequiredMixin, DeleteView):
    model = Veiculo
    template_name = 'veiculo/deletar.html'
    success_url = reverse_lazy('listar-veiculos')
            
class APIListarVeiculos(ListAPIView):
    serializer_class = SerializadorVeiculo
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Veiculo.objects.all()

class ApiDeletarVeiculos(DestroyAPIView):
    Serializer_class = SerializadorVeiculo
    authentication_classes = [TokenAuthentication]
    permissions_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Veiculo.objects.all()
    