# vehiculos/api_views.py
from rest_framework import viewsets, permissions
from vehiculos.models import Car, Brand, VehiculoReview
from vehiculos.serializers import CarSerializer, BrandSerializer, VehiculoReviewSerializer

class CarViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]

class BrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [permissions.IsAuthenticated]

class VehiculoReviewViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VehiculoReview.objects.all()
    serializer_class = VehiculoReviewSerializer
    permission_classes = [permissions.IsAuthenticated]
