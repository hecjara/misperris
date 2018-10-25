from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, label="Nombre")
    last_name = forms.CharField(required=True, label="Apellido")


    #fecha_nacimiento = forms.DateField(required=True, label="Fecha nacimiento")
    #run = forms.CharField(required=True, label="Run")
    #telefono = forms.IntegerField(required=True,label="Telefono")
    #region = forms.ComboField(required=True, label="Región")
    #ciudad = forms.ComboField(required=True, label="Ciudad")
    #tipo_vivienda = forms.ComboField(required=True, label="Tipo Vivienda")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

