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
    Cliente_Update,
    Cliente_Delete,
)

urlpatterns = [
    # USUARIOS
    path('', login_required(Usuario_View.as_view(), login_url='login'), name='usuario_list'),
    path('create/', login_required(Usuario_Create.as_view(), login_url='login'), name='usuario_create'),
    path('<int:pk>/detail/', login_required(Usuario_Detail.as_view(), login_url='login'), name='usuario_detail'),
    path('<int:pk>/update/', login_required(Usuario_Update.as_view(), login_url='login'), name='usuario_update'),
    path('<int:pk>/delete/', login_required(Usuario_Delete.as_view(), login_url='login'), name='usuario_delete'),

    # CLIENTES
    path('cliente/', login_required(Cliente_View.as_view(), login_url='login'), name='cliente_list'),
    path('cliente/create/', login_required(Cliente_Create.as_view(), login_url='login'), name='cliente_create'),
    path('cliente/<int:pk>/update/', login_required(Cliente_Update.as_view(), login_url='login'), name='cliente_update'),
    path('cliente/<int:pk>/delete/', login_required(Cliente_Delete.as_view(), login_url='login'), name='cliente_delete'),
]
