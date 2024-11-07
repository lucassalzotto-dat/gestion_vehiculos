from django.contrib import admin
from usuario.models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    search_fields = ('user__username', 'address', 'phone')
    list_display = ('user', 'address', 'phone')
    ordering = ('user',)  # Ordenar por nombre de usuario
