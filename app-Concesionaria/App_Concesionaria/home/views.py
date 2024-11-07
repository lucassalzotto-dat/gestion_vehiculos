from django.shortcuts import redirect, render
from django.contrib.auth import (
    authenticate,
    login, 
    logout,
)
from django.views import View
from usuario.forms import UserRegisterForm
# Create your views here.

#Rederiza el template de index.
def index_view(request):
    return render(
        request,
        'home.html'
    )

#Rederiza el template de login y verifica que los datos ingresados sea los correctos.
class LoginView(View):
    def get(self, request):
        return render(
            request,
            'login.html'
        )
    
    def post(self, request):    
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(
                request,
                username=username,
                password=password
            )
            if user:
                login(request, user)
                return redirect('index')
        return redirect('login')
    
#Retorna nuevamente al login
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')

#Rederiza el template de register y crea un nuevo registro con los datos ingresados, luego redirige al index.
class RegisterView(View):
    form_class = UserRegisterForm
    template_name = 'register.html'

    def get(self, request):
        form = self.form_class()
        return render(
            request,
            self.template_name,
            {
                'form':form
            }  
        )
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        return render(
            request,
            self.template_name,
            {
                'form':form
            }
        )


