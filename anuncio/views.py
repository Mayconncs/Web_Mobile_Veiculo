from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from anuncio.models import Anuncio
from anuncio.forms import FormularioAnuncio

class ListarAnuncios(LoginRequiredMixin, ListView):
    model = Anuncio
    context_object_name = 'anuncios'
    template_name = 'anuncio/listar.html'

class CriarAnuncio(LoginRequiredMixin, CreateView):
    model = Anuncio
    form_class = FormularioAnuncio
    template_name = 'anuncio/novo.html'
    success_url = reverse_lazy('listar-anuncios')

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super().form_valid(form)

class EditarAnuncio(LoginRequiredMixin, UpdateView):
    model = Anuncio
    form_class = FormularioAnuncio
    template_name = 'anuncio/editar.html'
    success_url = reverse_lazy('listar-anuncios')

class DeletarAnuncio(LoginRequiredMixin, DeleteView):
    model = Anuncio
    template_name = 'anuncio/deletar.html'
    success_url = reverse_lazy('listar-anuncios')