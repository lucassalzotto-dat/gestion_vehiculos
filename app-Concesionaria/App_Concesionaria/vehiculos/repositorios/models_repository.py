from vehiculos.models import Modelo
from .base_repository import BaseRepository

class ModelsRepository(BaseRepository):
    def __init__(self):
        super().__init__(Modelo)
