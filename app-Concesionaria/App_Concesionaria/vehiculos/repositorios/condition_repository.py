from vehiculos.models import Condition
from .base_repository import BaseRepository

class ConditionRepository(BaseRepository):
    def __init__(self):
        super().__init__(Condition)
