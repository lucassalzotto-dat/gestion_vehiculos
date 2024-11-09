# vehiculos/api_views.py
from rest_framework import viewsets, permissions
from vehiculos.models import (
    Car, Brand, VehiculoReview, Country, Modelo, Fuel, 
    Transmission, Gama, Condition, BodyWork
)
from vehiculos.serializers import (
    CarSerializer, BrandSerializer, VehiculoReviewSerializer, 
    CountrySerializer, ModeloSerializer, FuelSerializer, 
    TransmissionSerializer, GamaSerializer, ConditionSerializer, 
    BodyWorkSerializer
)

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [permissions.IsAuthenticated]

class VehiculoReviewViewSet(viewsets.ModelViewSet):
    queryset = VehiculoReview.objects.all()
    serializer_class = VehiculoReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticated]

class ModeloViewSet(viewsets.ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer
    permission_classes = [permissions.IsAuthenticated]

class FuelViewSet(viewsets.ModelViewSet):
    queryset = Fuel.objects.all()
    serializer_class = FuelSerializer
    permission_classes = [permissions.IsAuthenticated]

class TransmissionViewSet(viewsets.ModelViewSet):
    queryset = Transmission.objects.all()
    serializer_class = TransmissionSerializer
    permission_classes = [permissions.IsAuthenticated]

class GamaViewSet(viewsets.ModelViewSet):
    queryset = Gama.objects.all()
    serializer_class = GamaSerializer
    permission_classes = [permissions.IsAuthenticated]

class ConditionViewSet(viewsets.ModelViewSet):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer
    permission_classes = [permissions.IsAuthenticated]

class BodyWorkViewSet(viewsets.ModelViewSet):
    queryset = BodyWork.objects.all()
    serializer_class = BodyWorkSerializer
    permission_classes = [permissions.IsAuthenticated]
