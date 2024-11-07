from typing import List, Optional
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from usuario.models import Cliente

class Cliente_Repository:
    def get_all(self) -> List[Cliente]:
        return Cliente.objects.all()

    def create(self, user: User, address: str, phone: str) -> Cliente:
        return Cliente.objects.create(
            user=user, 
            address=address, 
            phone=phone
        )

    def delete(self, cliente: Cliente) -> None:
        cliente.delete()
        
    def update(self, cliente: Cliente, address: str, phone: str) -> Cliente:
        cliente.address = address
        cliente.phone = phone
        cliente.save()
        return cliente
    
    def get_by_id(self, id: int) -> Optional[Cliente]:
        return get_object_or_404(Cliente, id=id)
