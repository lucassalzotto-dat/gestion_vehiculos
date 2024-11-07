from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from vehiculos.forms import CarForm
from vehiculos.repositorios.vehiculos_repository import VehiculosRepository
# Importar el decorador en una vista de la aplicación vehiculos
from App_Concesionaria.decorators.decorators import staff_required

repository = VehiculosRepository()

def staff_required(user):
    return user.is_staff

@method_decorator(user_passes_test(staff_required, login_url='index'), name='dispatch')
class CarListView(View):
    def get(self, request):
        cars = repository.get_all()
        return render(request, 'car_list.html', {'cars': cars})

@method_decorator(user_passes_test(staff_required, login_url='index'), name='dispatch')
class CarCreateView(View):
    def get(self, request):
        form = CarForm()
        return render(request, 'car_create.html', {'form': form})
    
    def post(self, request):
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Guarda el objeto directamente en la base de datos
            return redirect('vehiculos_app:vehiculo_list')
        return render(request, 'car_create.html', {'form': form})

@method_decorator(user_passes_test(staff_required, login_url='index'), name='dispatch')
class CarDetailView(View):
    def get(self, request, id):
        car = repository.get_by_id(id)
        return render(request, 'car_detail.html', {'car': car})

@method_decorator(user_passes_test(staff_required, login_url='index'), name='dispatch')
class CarUpdateView(View):
    def get(self, request, id):
        car = repository.get_by_id(id)  # Asegúrate de que `repository.get_by_id` funcione correctamente
        form = CarForm(instance=car)
        return render(request, 'car_update.html', {'form': form, 'car': car})
    
    def post(self, request, id):
        car = repository.get_by_id(id)
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            repository.update(car, **form.cleaned_data)
            return redirect('vehiculos_app:car_detail', id=id)  # Usar el nombre de la vista
        return render(request, 'car_update.html', {'form': form, 'car': car})

@method_decorator(user_passes_test(staff_required, login_url='index'), name='dispatch')
class CarDeleteView(View):
    def get(self, request, id):
        car = repository.get_by_id(id)
        repository.delete(car)
        return redirect('vehiculos_app:vehiculo_list')
