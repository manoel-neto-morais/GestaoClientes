from django.urls import path
from .views import *


urlpatterns = [
    path('list/', persons_list, name='listar'),
    path('new/', persons_new, name='cadastrar'),
    path('update/<int:id>/', persons_update, name='atualizar'),
    path('delete/<int:id>/', persons_delete, name='deletar')#essa rota passará um número inteiro na qual reconheceremos o campo no banco de dados
]



