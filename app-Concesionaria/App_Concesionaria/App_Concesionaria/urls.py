from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', include('usuario.urls')),    # Rutas de la aplicación usuario
    path('vehiculos/', include('vehiculos.urls')), # Rutas de la aplicación vehiculos
    path('', include('home.urls')),                # Rutas de la aplicación home, raíz de la página
]
