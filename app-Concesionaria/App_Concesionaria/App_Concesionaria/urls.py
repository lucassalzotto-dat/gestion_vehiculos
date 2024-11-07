from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', include('usuario.urls')),    # Rutas de la aplicación usuario
    path('vehiculos/', include('vehiculos.urls')), # Rutas de la aplicación vehiculos
    path('', include('home.urls')),                # Rutas de la aplicación home, raíz de la página
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

