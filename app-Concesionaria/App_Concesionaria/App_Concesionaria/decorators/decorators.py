from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied

def staff_required(view_func):
    """
    Decorador para asegurarse de que el usuario es staff.
    Redirige a la página de inicio o lanza una excepción de permiso denegado si no es staff.
    """
    decorated_view_func = user_passes_test(
        lambda u: u.is_staff,
        login_url='index'  # Cambia 'index' a la URL que deseas usar para redirigir en caso de acceso denegado
    )(view_func)
    
    return decorated_view_func
