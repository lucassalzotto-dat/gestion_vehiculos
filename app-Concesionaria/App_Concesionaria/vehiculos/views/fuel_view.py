from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from vehiculos.forms import FuelForm
from vehiculos.repositorios.fuel_repository import FuelRepository
# Importar el decorador en una vista de la aplicación vehiculos
from App_Concesionaria.decorators.decorators import staff_required

repository = FuelRepository()

def staff_required(user):
    return user.is_staff

@method_decorator(user_passes_test(staff_required, login_url='index'), name='dispatch')
class FuelListView(View):
    def get(self, request):
        fuels = repository.get_all()
        return render(request, 'vehiculos/fuel_list.html', {'fuels': fuels})

@method_decorator(user_passes_test(staff_required, login_url='index'), name='dispatch')
class FuelCreateView(View):
    def get(self, request):
        form = FuelForm()
        return render(request, 'vehiculos/fuel_create.html', {'form': form})
    
    def post(self, request):
        form = FuelForm(request.POST)
        if form.is_valid():
            repository.create(**form.cleaned_data)
            return redirect('fuel_list')
        return render(request, 'vehiculos/fuel_create.html', {'form': form})

@method_decorator(user_passes_test(staff_required, login_url='index'), name='dispatch')
class FuelDeleteView(View):
    def get(self, request, id):
        fuel = repository.get_by_id(id)
        repository.delete(fuel)
        return redirect('fuel_list')
