from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cliente_profile')
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username

    @property
    def is_cliente(self):
        return True

# Agregar propiedad directamente a la clase User
User.add_to_class('is_cliente', property(lambda u: hasattr(u, 'cliente_profile')))
