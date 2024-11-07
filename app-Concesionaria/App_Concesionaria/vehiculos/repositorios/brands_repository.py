from vehiculos.models import Brand
from .base_repository import BaseRepository

class BrandsRepository(BaseRepository):
    def __init__(self):
        super().__init__(Brand)
