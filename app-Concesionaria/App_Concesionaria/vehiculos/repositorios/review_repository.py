from vehiculos.models import VehiculoReview
from .base_repository import BaseRepository

class ReviewRepository(BaseRepository):
    def __init__(self):
        super().__init__(VehiculoReview)
