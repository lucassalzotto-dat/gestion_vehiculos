# vehiculos/serializers.py
from rest_framework import serializers
from vehiculos.models import Car, Brand, VehiculoReview

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']

class CarSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()

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
