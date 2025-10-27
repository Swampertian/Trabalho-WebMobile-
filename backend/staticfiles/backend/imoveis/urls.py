from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *


urlpatterns = [
    # Urls de renderização no template Engine :()
    path('', login_required(ListarImoveis.as_view(),login_url='login'), name='home'),
    path('cadastrar/',login_required(CadastrarImovel.as_view(),login_url='login'), name='cadastrar-veiculos'),
    path('editar/<int:pk>/',login_required(EditarImovel.as_view(),login_url='login'), name='editar-veiculos'),
    path('excluir/<int:pk>/',login_required(ExcluirImovel.as_view(),login_url='login'), name='excluir-veiculos'),
    path('fotos/<str:arquivo>/',FotosImoveis.as_view(), name='fotos-veiculo'),
]