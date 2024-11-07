from vehiculos.models import Country
from .base_repository import BaseRepository

class CountriesRepository(BaseRepository):
    def __init__(self):
        super().__init__(Country)
