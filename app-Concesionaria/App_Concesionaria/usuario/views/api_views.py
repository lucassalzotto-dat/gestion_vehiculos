# usuario/api_views.py
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from usuario.models import Cliente
from usuario.serializers import UserSerializer, ClienteSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
