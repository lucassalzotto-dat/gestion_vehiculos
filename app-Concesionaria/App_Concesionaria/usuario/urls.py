from django.urls import path
from django.contrib.auth.decorators import login_required

from usuario.views.usuarios_view import (
    Usuario_View,
    Usuario_Create,
    Usuario_Detail,
    Usuario_Update,
    Usuario_Delete,
)
from usuario.views.clientes_view import (
    Cliente_View,
    Cliente_Create,
)

urlpatterns = [
    # USUARIOS
    path('usuarios/', login_required(Usuario_View.as_view(), login_url='login'), name='usuario_list'),
    path('usuarios/create/', login_required(Usuario_Create.as_view(), login_url='login'), name='usuario_create'),
    path('usuarios/<int:id>/detail/', login_required(Usuario_Detail.as_view(), login_url='login'), name='usuario_detail'),
    path('usuarios/<int:id>/update/', login_required(Usuario_Update.as_view(), login_url='login'), name='usuario_update'),
    path('usuarios/<int:id>/delete/', login_required(Usuario_Delete.as_view(), login_url='login'), name='usuario_delete'),

    # CLIENTES
    path('clientes/', login_required(Cliente_View.as_view(), login_url='login'), name='cliente_list'),
    path('clientes/create/', login_required(Cliente_Create.as_view(), login_url='login'), name='cliente_create'),
    path('clientes/<int:id>/update/', login_required(Cliente_Create.as_view(), login_url='login'), name='cliente_update'),
    path('clientes/<int:id>/delete/', login_required(Cliente_Create.as_view(), login_url='login'), name='cliente_delete'),
]
