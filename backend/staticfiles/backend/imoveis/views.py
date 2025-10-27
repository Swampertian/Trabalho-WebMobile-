from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from .models import Imoveis
from .forms import ImoveisForm
from django.urls import reverse_lazy

class ListarImoveis(ListView):
    model = Imoveis
    template_name = 'home.html'
    context_object_name = 'imoveis_list'

class CadastrarImovel(CreateView):
    model = Imoveis
    form_class = ImoveisForm
    contexto = 'imoveis'
    template_name = 'imoveis/cadastrar_imovel.html'
    success_url = reverse_lazy('listar_imoveis')

class EditarImovel(UpdateView):
    model = Imoveis
    form_class = ImoveisForm
    contexto = 'imoveis'
    template_name = 'imoveis/editar_imovel.html'
    success_url = reverse_lazy('listar_imoveis')

class ExcluirImovel(DeleteView):
    model = Imoveis
    contexto = 'imoveis'
    template_name = 'alert.html'
    success_url = reverse_lazy('listar_imoveis')

class FotosImoveis(View):
    def get(self, request, pk):
        imovel = Imoveis.objects.get(pk=pk)
        contexto = {
            'imovel': imovel
        }
        return render(request, 'imoveis/fotos_imovel.html', contexto)