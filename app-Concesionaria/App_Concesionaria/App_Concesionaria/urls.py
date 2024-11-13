from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuración de Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="API de Concesionaria",
        default_version="v1",
        description="Documentación de la API de la aplicación de concesionaria",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="soporte@concesionaria.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("usuario/", include("usuario.urls")),
    path("vehiculos/", include("vehiculos.urls")),
    path("", include("home.urls")),  # Ruta principal de la página de inicio
    path("i18n/", include("django.conf.urls.i18n")),  # Ruta para cambiar el idioma

    # URLs para Swagger
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
