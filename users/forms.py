from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import timedelta

from .models import Perfil, IntentoLogin


class FormularioRegistro(UserCreationForm): 
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class FormularioAcceso(AuthenticationForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Username', 'class': 'form-control'
    }))

    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'form-control',
        'data-toggle': 'password',
        'id': 'password',
        'name': 'password'
    }))

    remember_me = forms.BooleanField(required=False)

    MAX_INTENTOS = 5
    MINUTOS_BLOQUEO = 15

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            intento, _ = IntentoLogin.objects.get_or_create(username=username)

            if intento.bloqueado_hasta and intento.bloqueado_hasta > timezone.now():
                raise forms.ValidationError(
                    f"Usuario bloqueado temporalmente hasta "
                    f"{intento.bloqueado_hasta.strftime('%Y-%m-%d %H:%M')} "
                    f"por varios intentos fallidos."
                )

            self.user_cache = authenticate(
                self.request,
                username=username,
                password=password
            )

            if self.user_cache is None:
                intento.intentos_fallidos += 1

                usuario = User.objects.filter(username=username).first()
                if usuario:
                    intento.usuario = usuario

                if intento.intentos_fallidos >= self.MAX_INTENTOS:
                    intento.bloqueado_hasta = timezone.now() + timedelta(
                        minutes=self.MINUTOS_BLOQUEO
                    )

                intento.save()
                raise self.get_invalid_login_error()

            intento.usuario = self.user_cache
            intento.intentos_fallidos = 0
            intento.bloqueado_hasta = None
            intento.save()

            self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


class FormularioActualizarUsuario(forms.ModelForm): 
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class FormularioActualizarPerfil(forms.ModelForm): 
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Perfil 
        fields = ['bio']