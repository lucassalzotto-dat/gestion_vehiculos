from django.contrib.auth.models import User
from random import choice

def user_info(request):
    if request.user.is_authenticated:
        return {'user_info': {
            'name': request.user.first_name,  # Obtén el nombre completo del usuario
        }}
    return {}
