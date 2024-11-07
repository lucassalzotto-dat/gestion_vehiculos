from vehiculos.models import Fuel
from .base_repository import BaseRepository

class FuelRepository(BaseRepository):
    def __init__(self):
        super().__init__(Fuel)
