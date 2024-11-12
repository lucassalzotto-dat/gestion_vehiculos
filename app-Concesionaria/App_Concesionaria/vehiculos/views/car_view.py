from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from vehiculos.forms import CarForm, ReviewForm
from vehiculos.models import Car, VehiculoReview 
from vehiculos.repositorios.vehiculos_repository import VehiculosRepository
from django.contrib.auth.mixins import LoginRequiredMixin
from App_Concesionaria.decorators.decorators import staff_required

repository = VehiculosRepository()

# Vista para mostrar la lista de vehículos, accesible para todos
class CarListView(View):
    def get(self, request):
        cars = repository.get_all()
        return render(request, 'car_list.html', {'cars': cars})

# Vista para ver los detalles de un vehículo y agregar reseñas, accesible para todos
class CarDetailView(View):
    def get(self, request, id):
        car = repository.get_by_id(id)
        reviews = VehiculoReview.objects.filter(vehiculo=car)
        review_form = ReviewForm()  # Formulario para reseñas
        return render(request, 'car_detail.html', {'car': car, 'reviews': reviews, 'review_form': review_form})

# Solo staff puede crear vehículos
@method_decorator(user_passes_test(staff_required, login_url='index'), name='dispatch')
class CarCreateView(View):
    def get(self, request):
        form = CarForm()
        return render(request, 'car_create.html', {'form': form})

    def post(self, request):
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            repository.create(**form.cleaned_data)
            return redirect('vehiculos_app:vehiculo_list')
        return render(request, 'car_create.html', {'form': form})

# Solo staff puede actualizar vehículos
@method_decorator(user_passes_test(staff_required, login_url='index'), name='dispatch')
class CarUpdateView(View):
    def get(self, request, id):
        car = repository.get_by_id(id)
        form = CarForm(instance=car)
        return render(request, 'car_update.html', {'form': form, 'car': car})

    def post(self, request, id):
        car = repository.get_by_id(id)
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            repository.update(car, **form.cleaned_data)
            return redirect('vehiculos_app:car_detail', id=id)
        return render(request, 'car_update.html', {'form': form, 'car': car})

# Solo staff puede eliminar vehículos
@method_decorator(user_passes_test(staff_required, login_url='index'), name='dispatch')
class CarDeleteView(View):
    def get(self, request, id):
        car = repository.get_by_id(id)
        repository.delete(car)
        return redirect('vehiculos_app:vehiculo_list')

# Solo usuarios logueados pueden dejar reseñas
class AddReviewView(LoginRequiredMixin, View):
    def post(self, request, car_id):
        car = get_object_or_404(Car, id=car_id)
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.vehiculo = car
            review.author = request.user
            review.save()
            return redirect('vehiculos_app:car_detail', id=car.id)
        reviews = VehiculoReview.objects.filter(vehiculo=car)
        return render(request, 'car_detail.html', {'car': car, 'reviews': reviews, 'review_form': form})
