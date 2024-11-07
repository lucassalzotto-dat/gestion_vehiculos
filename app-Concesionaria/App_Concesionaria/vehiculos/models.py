from django.db import models
from django.contrib.auth.models import User

class Country(models.Model):
    name = models.CharField(max_length=200)
  
    def __str__(self):
        return self.name

class Modelo(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=200)
  
    def __str__(self):
        return self.name

class Fuel(models.Model):
    name = models.CharField(max_length=200)
  
    def __str__(self):
        return self.name

class Transmission(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Gama(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Condition(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class BodyWork(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Car(models.Model):
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name='cars',
    )
    model_car = models.ForeignKey(
        Modelo,
        on_delete=models.CASCADE,
        related_name='cars',
    )
    year_production = models.CharField(max_length=4)
    door_quantity = models.IntegerField()
    cilindrada = models.IntegerField()
    fuel_type = models.ForeignKey(
        Fuel,
        on_delete=models.CASCADE,
        related_name='cars',
    )
    country_production = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name='cars',
    )
    image = models.ImageField(upload_to='vehiculos_images/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    km = models.IntegerField(default=0)
    transmission = models.ForeignKey(
        Transmission,
        on_delete=models.CASCADE,
        related_name='cars',
    )
    gama = models.ForeignKey(
        Gama,
        on_delete=models.CASCADE,
        related_name='cars',
    )
    condition = models.ForeignKey(
        Condition,
        on_delete=models.CASCADE,
        related_name='cars',
    )
    body_work = models.ForeignKey(
        BodyWork,
        on_delete=models.CASCADE,
        related_name='cars',
    )

    def __str__(self):
        return f"{self.brand.name} {self.model_car.name} ({self.year_production})"
  
    def info_car(self):
        return f"{self.brand.name} {self.model_car.name}, Año {self.year_production}"

class VehiculoReview(models.Model):
    vehiculo = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=1, choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return f'Review by {self.author.username} for {self.vehiculo.brand.name}'
