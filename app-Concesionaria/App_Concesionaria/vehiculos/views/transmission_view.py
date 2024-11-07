from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from vehiculos.forms import TransmissionForm
from vehiculos.repositorios.transmission_repository import TransmissionRepository
from App_Concesionaria.decorators.decorators import staff_required
repository = TransmissionRepository()

@method_decorator(user_passes_test(staff_required, login_url='index'), name='dispatch')
class TransmissionListView(View):
    def get(self, request):
        transmissions = repository.get_all()
        return render(request, 'vehiculos/transmission_list.html', {'transmissions': transmissions})

@method_decorator(user_passes_test(staff_required, login_url='index'), name='dispatch')
class TransmissionCreateView(View):
    def get(self, request):
        form = TransmissionForm()
        return render(request, 'vehiculos/transmission_create.html', {'form': form})
    
    def post(self, request):
        form = TransmissionForm(request.POST)
        if form.is_valid():
            repository.create(**form.cleaned_data)
            return redirect('transmission_list')
        return render(request, 'vehiculos/transmission_create.html', {'form': form})

@method_decorator(user_passes_test(staff_required, login_url='index'), name='dispatch')
class TransmissionDeleteView(View):
    def get(self, request, id):
        transmission = repository.get_by_id(id)
        repository.delete(transmission)
        return redirect('transmission_list')
