from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from vehiculos.forms import ModelForm
from vehiculos.repositorios.models_repository import ModelsRepository
from App_Concesionaria.decorators.decorators import staff_required
repository = ModelsRepository()

@method_decorator(user_passes_test(staff_required, login_url='index'), name='dispatch')
class ModelListView(View):
    def get(self, request):
        models = repository.get_all()
        return render(request, 'vehiculos/model_list.html', {'models': models})

@method_decorator(user_passes_test(staff_required, login_url='index'), name='dispatch')
class ModelCreateView(View):
    def get(self, request):
        form = ModelForm()
        return render(request, 'vehiculos/model_create.html', {'form': form})
    
    def post(self, request):
        form = ModelForm(request.POST)
        if form.is_valid():
            repository.create(**form.cleaned_data)
            return redirect('model_list')
        return render(request, 'vehiculos/model_create.html', {'form': form})