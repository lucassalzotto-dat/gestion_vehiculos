from typing import List, Optional
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class Usuario_Repository:
    def get_all(self) -> List[User]:
        return User.objects.all()
        
    def delete(self, usuario: User) -> None:
        usuario.delete()
    
    def get_by_id(self, id: int) -> Optional[User]:
        return get_object_or_404(User, id=id)
