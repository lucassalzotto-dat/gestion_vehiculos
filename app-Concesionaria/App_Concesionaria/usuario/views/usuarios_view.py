from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from usuario.repositorios.usuarios_repositories import Usuario_Repository
from usuario.forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth import login
from usuario.forms import RegisterForm

repository = Usuario_Repository()

def staff_required(user):
    return user.is_staff

@method_decorator(user_passes_test(staff_required, login_url='index'), name='dispatch')
class Usuario_View(View):
    def get(self, request):
        usuarios = repository.get_all()
        return render(request, 'usuarios/list.html', {'usuarios': usuarios})

@method_decorator(user_passes_test(staff_required, login_url='index'), name='dispatch')
class Usuario_Create(View):
    form_class = UserRegisterForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'usuarios/create.html', {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('usuario_app:usuario_list')
        return render(request, 'usuarios/list.html', {'form': form})

@method_decorator(user_passes_test(staff_required, login_url='index'), name='dispatch')
class Usuario_Detail(View):
    def get(self, request, id):
        usuario = repository.get_by_id(id=id)
        return render(request, 'usuarios/details.html', {'usuario': usuario})

@method_decorator(user_passes_test(staff_required, login_url='index'), name='dispatch')
class Usuario_Delete(View):
    def get(self, request, id):
        usuario = repository.get_by_id(id=id)
        if usuario:
            repository.delete(usuario)
        return redirect('usuario_app:usuario_list')

@method_decorator(user_passes_test(staff_required, login_url='index'), name='dispatch')
class Usuario_Update(View):
    form_class = UserUpdateForm

    def get(self, request, id):
        usuario = repository.get_by_id(id=id)
        user_form = self.form_class(instance=usuario)
        return render(request, 'usuarios/update.html', {'user_form': user_form, 'usuario': usuario})

    def post(self, request, id):
        usuario = repository.get_by_id(id=id)
        user_form = self.form_class(request.POST, instance=usuario)
        if user_form.is_valid():
            user_form.save()
            return redirect('usuario_app:usuario_detail', id=id)
        return render(request, 'usuarios/update.html', {'user_form': user_form, 'usuario': usuario})


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'usuarios/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('vehiculos_app:vehiculo_list')
        return render(request, 'usuarios/register.html', {'form': form})
