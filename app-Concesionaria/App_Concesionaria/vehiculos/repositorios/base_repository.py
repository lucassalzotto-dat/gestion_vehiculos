from typing import List, TypeVar, Type, Optional
from django.db import models
from django.shortcuts import get_object_or_404

T = TypeVar('T', bound=models.Model)

class BaseRepository:
    model: Type[T]

    def __init__(self, model: Type[T]):
        self.model = model

    def get_all(self) -> List[T]:
        return self.model.objects.all()

    def get_by_id(self, id: int) -> Optional[T]:
        return get_object_or_404(self.model, id=id)

    def create(self, **kwargs) -> T:
        return self.model.objects.create(**kwargs)

    def update(self, instance: T, **kwargs) -> T:
        for key, value in kwargs.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    def delete(self, instance: T) -> None:
        instance.delete()
