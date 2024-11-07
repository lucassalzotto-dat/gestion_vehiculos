from vehiculos.models import BodyWork
from .base_repository import BaseRepository

class BodyWorkRepository(BaseRepository):
    def __init__(self):
        super().__init__(BodyWork)
