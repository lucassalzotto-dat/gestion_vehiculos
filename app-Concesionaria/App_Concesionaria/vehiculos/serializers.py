# vehiculos/serializers.py
from rest_framework import serializers
from vehiculos.models import (
    Car, Brand, VehiculoReview, Country, Modelo, Fuel, 
    Transmission, Gama, Condition, BodyWork
)

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']

class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo
        fields = ['id', 'name']

class FuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuel
        fields = ['id', 'name']

class TransmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transmission
        fields = ['id', 'name']

class GamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gama
        fields = ['id', 'name']

class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = ['id', 'name']

class BodyWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyWork
        fields = ['id', 'name']

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']

class CarSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    model_car = ModeloSerializer()
    fuel_type = FuelSerializer()
    country_production = CountrySerializer()
    transmission = TransmissionSerializer()
    gama = GamaSerializer()
    condition = ConditionSerializer()
    body_work = BodyWorkSerializer()

    class Meta:
        model = Car
        fields = [
            'id', 'brand', 'model_car', 'year_production', 'door_quantity', 
            'cilindrada', 'fuel_type', 'country_production', 'image', 'price',
            'km', 'transmission', 'gama', 'condition', 'body_work'
        ]

class VehiculoReviewSerializer(serializers.ModelSerializer):
    vehiculo = CarSerializer()
    author = serializers.StringRelatedField()

    class Meta:
        model = VehiculoReview
        fields = ['id', 'vehiculo', 'author', 'text', 'date', 'rating']
