from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from usuario.forms import ClienteForm
from usuario.repositorios.clientes_repositories import Cliente_Repository

repository = Cliente_Repository()

def staff_required(user):
    return user.is_staff

@method_decorator(user_passes_test(staff_required, login_url='index'), name='dispatch')
class Cliente_View(View):
    def get(self, request):
        clientes = repository.get_all()  # Obtener todos los clientes del repositorio
        return render(request, 'clientes/list.html', {'clientes': clientes})

@method_decorator(user_passes_test(staff_required, login_url='index'), name='dispatch')
class Cliente_Create(View):
    def get(self, request):
        form = ClienteForm()
        users = User.objects.all()
        return render(request, 'clientes/create.html', {'form': form, 'users': users})

    def post(self, request):
        form = ClienteForm(request.POST)
        if form.is_valid():
            user_id = request.POST.get('user')
            user = get_object_or_404(User, id=user_id)  # Asegura que el usuario existe
            nuevo_cliente = repository.create(
                user=user,
                address=form.cleaned_data['address'],
                phone=form.cleaned_data['phone']
            )
            return redirect('cliente_list')
        users = User.objects.all()  # Agregar los usuarios de nuevo en caso de que el formulario no sea válido
        return render(request, 'clientes/create.html', {'form': form, 'users': users})
@method_decorator(user_passes_test(staff_required, login_url='index'), name='dispatch')
class Cliente_Delete(View):
    def get(self, request, id):
        cliente = repository.get_by_id(id=id)
        if cliente:
            repository.delete(cliente)
        return redirect('cliente_list')

@method_decorator(user_passes_test(staff_required, login_url='index'), name='dispatch')
class Cliente_Update(View):
    def get(self, request, id):
        cliente = repository.get_by_id(id=id)
        form = ClienteForm(instance=cliente)
        return render(request, 'clientes/update.html', {'form': form, 'cliente': cliente})

    def post(self, request, id):
        cliente = repository.get_by_id(id=id)
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            repository.update(
                cliente=cliente,
                address=form.cleaned_data['address'],
                phone=form.cleaned_data['phone']
            )
            return redirect('cliente_list')
        return render(request, 'cliente/update.html', {'form': form, 'cliente': cliente})