# usuario/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth.decorators import login_required
from usuario.views.usuarios_view import (
    Usuario_View, Usuario_Create, Usuario_Detail, Usuario_Update, Usuario_Delete, RegisterView
)
from usuario.views.clientes_view import Cliente_View, Cliente_Create, Cliente_Update, Cliente_Delete
from usuario.views.api_views import UserViewSet, ClienteViewSet

app_name = 'usuario_app'
router = DefaultRouter()
router.register(r'api/usuarios', UserViewSet)
router.register(r'api/clientes', ClienteViewSet)

urlpatterns = [
    # Rutas de vistas basadas en clases
    path('usuarios/register/', RegisterView.as_view(), name='register'),
    path('usuarios/', Usuario_View.as_view(), name='usuario_list'),
    path('usuarios/create/', Usuario_Create.as_view(), name='usuario_create'),
    path('usuarios/<int:id>/detail/', Usuario_Detail.as_view(), name='usuario_detail'),
    path('usuarios/<int:id>/update/', Usuario_Update.as_view(), name='usuario_update'),
    path('usuarios/<int:id>/delete/', Usuario_Delete.as_view(), name='usuario_delete'),
    path('cliente/', login_required(Cliente_View.as_view(), login_url='login'), name='cliente_list'),
    path('cliente/create/', login_required(Cliente_Create.as_view(), login_url='login'), name='cliente_create'),
    path('cliente/<int:id>/update/', login_required(Cliente_Update.as_view(), login_url='login'), name='cliente_update'),
    path('cliente/<int:id>/delete/', Cliente_Delete.as_view(), name='cliente_delete'),
    
    # Rutas de la API
    path('', include(router.urls)),
]
