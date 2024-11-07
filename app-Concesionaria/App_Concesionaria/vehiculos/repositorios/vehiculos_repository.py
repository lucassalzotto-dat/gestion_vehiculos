from vehiculos.models import Car
from .base_repository import BaseRepository

class VehiculosRepository(BaseRepository):
    def __init__(self):
        super().__init__(Car)
