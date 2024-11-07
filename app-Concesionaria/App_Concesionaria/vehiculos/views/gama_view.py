from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from vehiculos.forms import GamaForm
from vehiculos.repositorios.gama_repository import GamaRepository
# Importar el decorador en una vista de la aplicación vehiculos
from App_Concesionaria.decorators.decorators import staff_required

repository = GamaRepository()

@method_decorator(user_passes_test(staff_required, login_url='index'), name='dispatch')
class GamaListView(View):
    def get(self, request):
        gamas = repository.get_all()
        return render(request, 'vehiculos/gama_list.html', {'gamas': gamas})

@method_decorator(user_passes_test(staff_required, login_url='index'), name='dispatch')
class GamaCreateView(View):
    def get(self, request):
        form = GamaForm()
        return render(request, 'vehiculos/gama_create.html', {'form': form})
    
    def post(self, request):
        form = GamaForm(request.POST)
        if form.is_valid():
            repository.create(**form.cleaned_data)
            return redirect('gama_list')
        return render(request, 'vehiculos/gama_create.html', {'form': form})

@method_decorator(user_passes_test(staff_required, login_url='index'), name='dispatch')
class GamaDeleteView(View):
    def get(self, request, id):
        gama = repository.get_by_id(id)
        repository.delete(gama)
        return redirect('gama_list')
