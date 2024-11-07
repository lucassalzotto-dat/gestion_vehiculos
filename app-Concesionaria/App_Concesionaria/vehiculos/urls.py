from django.urls import path
from vehiculos.views.car_view import CarListView, CarCreateView, CarDetailView, CarUpdateView, CarDeleteView
from vehiculos.views.fuel_view import FuelListView, FuelCreateView, FuelDeleteView
from vehiculos.views.transmission_view import TransmissionListView, TransmissionCreateView, TransmissionDeleteView
from vehiculos.views.gama_view import GamaListView, GamaCreateView, GamaDeleteView
from vehiculos.views.country_view import CountryListView, CountryCreateView, CountryDeleteView

app_name = 'vehiculos_app'

urlpatterns = [

    # Car (renombrado car_list a vehiculo_list)
    path('cars/', CarListView.as_view(), name='vehiculo_list'),
    path('cars/create/', CarCreateView.as_view(), name='car_create'),
    path('cars/<int:id>/', CarDetailView.as_view(), name='car_detail'),
    path('cars/<int:id>/update/', CarUpdateView.as_view(), name='car_update'),
    path('cars/<int:id>/delete/', CarDeleteView.as_view(), name='car_delete'),

    # Fuel
    path('fuel/', FuelListView.as_view(), name='fuel_list'),
    path('fuel/create/', FuelCreateView.as_view(), name='fuel_create'),
    path('fuel/<int:id>/delete/', FuelDeleteView.as_view(), name='fuel_delete'),

    # Transmission
    path('transmissions/', TransmissionListView.as_view(), name='transmission_list'),
    path('transmissions/create/', TransmissionCreateView.as_view(), name='transmission_create'),
    path('transmissions/<int:id>/delete/', TransmissionDeleteView.as_view(), name='transmission_delete'),

    # Gama
    path('gamas/', GamaListView.as_view(), name='gama_list'),
    path('gamas/create/', GamaCreateView.as_view(), name='gama_create'),
    path('gamas/<int:id>/delete/', GamaDeleteView.as_view(), name='gama_delete'),

    # Country
    path('countries/', CountryListView.as_view(), name='country_list'),
    path('countries/create/', CountryCreateView.as_view(), name='country_create'),
    path('countries/<int:id>/delete/', CountryDeleteView.as_view(), name='country_delete'),
]
