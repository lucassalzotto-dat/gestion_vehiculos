# usuario/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from usuario.models import Cliente

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class ClienteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Cliente
        fields = ['id', 'user', 'address', 'phone']
