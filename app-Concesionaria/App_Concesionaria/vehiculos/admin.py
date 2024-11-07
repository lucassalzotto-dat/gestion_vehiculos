from django.contrib import admin
from vehiculos.models import Car, Modelo, Brand, Fuel, Country, Transmission, Gama, Condition, BodyWork
from django.utils.html import format_html

# Registro del modelo Car en el panel de administración
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ('brand__name', 'model_car__name', 'year_production', 'country_production__name')
    list_filter = ('brand', 'cilindrada', 'fuel_type', 'door_quantity')
    list_editable = ('price',)
    empty_value_display = "No hay datos para este campo"

    list_display = (
        'brand',
        'model_car',
        'year_production',
        'door_quantity',
        'cilindrada',
        'fuel_type',
        'country_production',
        'image',
        'price',
    )



@admin.register(Modelo)
class ModeloAdmin(admin.ModelAdmin):
    empty_value_display = "No hay datos para este campo"
    list_display = ('name',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    empty_value_display = "No hay datos para este campo"
    list_display = ('name',)

@admin.register(Fuel)
class FuelAdmin(admin.ModelAdmin):
    empty_value_display = "No hay datos para este campo"
    list_display = ('name',)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    empty_value_display = "No hay datos para este campo"
    list_display = ('name',)

@admin.register(Transmission)
class CountryAdmin(admin.ModelAdmin):
    empty_value_display = "No hay datos para este campo"
    list_display = ('name',)

@admin.register(Gama)
class CountryAdmin(admin.ModelAdmin):
    empty_value_display = "No hay datos para este campo"
    list_display = ('name',)
    
@admin.register(Condition)
class CountryAdmin(admin.ModelAdmin):
    empty_value_display = "No hay datos para este campo"
    list_display = ('name',)

@admin.register(BodyWork)
class CountryAdmin(admin.ModelAdmin):
    empty_value_display = "No hay datos para este campo"
    list_display = ('name',)
