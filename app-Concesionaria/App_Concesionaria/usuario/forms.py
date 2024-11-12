from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Cliente
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Email Requerido')

    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2', 'first_name', 'last_name'
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control custom-class'}),
            'email': forms.EmailInput(attrs={'class': 'form-control custom-class'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control custom-class'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control custom-class'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control custom-class', 'required': 'required'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control custom-class', 'required': 'required'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("El email ya se encuentra registrado")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 != password2:
            raise ValidationError("Las contraseñas no coinciden")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.is_staff = False
        user.is_superuser = False
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control custom-class'}),
        required=False,
        help_text='Ingrese una nueva contraseña si desea cambiarla'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control custom-class'}),
        required=False,
        help_text='Confirme la nueva contraseña'
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control custom-class'}),
            'email': forms.EmailInput(attrs={'class': 'form-control custom-class'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control custom-class'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control custom-class'}),
        }
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        usuario_id = self.instance.id
        if User.objects.filter(email=email).exclude(id=usuario_id).exists():
            raise ValidationError("El email ya se encuentra registrado")
        return email
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Las contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        if self.cleaned_data.get('password1'):
            user.set_password(self.cleaned_data.get('password1'))
        if commit:
            user.save()
        return user

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['address', 'phone']
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control custom-class'}),
            'phone': forms.TextInput(attrs={'class': 'form-control custom-class'}),
        }


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
