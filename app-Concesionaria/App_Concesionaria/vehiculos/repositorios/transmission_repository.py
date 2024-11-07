from vehiculos.models import Transmission
from .base_repository import BaseRepository

class TransmissionRepository(BaseRepository):
    def __init__(self):
        super().__init__(Transmission)
