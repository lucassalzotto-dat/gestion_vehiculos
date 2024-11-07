from vehiculos.models import Gama
from .base_repository import BaseRepository

class GamaRepository(BaseRepository):
    def __init__(self):
        super().__init__(Gama)
