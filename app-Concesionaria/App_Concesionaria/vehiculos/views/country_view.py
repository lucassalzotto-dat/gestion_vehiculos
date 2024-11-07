from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from vehiculos.forms import CountryForm
from vehiculos.repositorios.countries_repository import CountriesRepository
# Importar el decorador en una vista de la aplicación vehiculos
from App_Concesionaria.decorators.decorators import staff_required

repository = CountriesRepository()

@method_decorator(user_passes_test(staff_required, login_url='index'), name='dispatch')
class CountryListView(View):
    def get(self, request):
        countries = repository.get_all()
        return render(request, 'vehiculos/country_list.html', {'countries': countries})

@method_decorator(user_passes_test(staff_required, login_url='index'), name='dispatch')
class CountryCreateView(View):
    def get(self, request):
        form = CountryForm()
        return render(request, 'vehiculos/country_create.html', {'form': form})
    
    def post(self, request):
        form = CountryForm(request.POST)
        if form.is_valid():
            repository.create(**form.cleaned_data)
            return redirect('country_list')
        return render(request, 'vehiculos/country_create.html', {'form': form})

@method_decorator(user_passes_test(staff_required, login_url='index'), name='dispatch')
class CountryDeleteView(View):
    def get(self, request, id):
        country = repository.get_by_id(id)
        repository.delete(country)
        return redirect('country_list')
