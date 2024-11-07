from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from vehiculos.forms import BrandForm
from vehiculos.repositorios.brands_repository import BrandsRepository
# Importar el decorador en una vista de la aplicación vehiculos
from App_Concesionaria.decorators.decorators import staff_required


repository = BrandsRepository()

@method_decorator(user_passes_test(staff_required, login_url='index'), name='dispatch')
class BrandListView(View):
    def get(self, request):
        brands = repository.get_all()
        return render(request, 'vehiculos/brand_list.html', {'brands': brands})

@method_decorator(user_passes_test(staff_required, login_url='index'), name='dispatch')
class BrandCreateView(View):
    def get(self, request):
        form = BrandForm()
        return render(request, 'vehiculos/brand_create.html', {'form': form})
    
    def post(self, request):
        form = BrandForm(request.POST)
        if form.is_valid():
            repository.create(**form.cleaned_data)
            return redirect('brand_list')
        return render(request, 'vehiculos/brand_create.html', {'form': form})
