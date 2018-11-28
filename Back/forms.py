from django import forms 
from .models import Mascota
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm

class Login(forms.Form):
    username=forms.CharField(widget=forms.TextInput(), label="Usuario")
    password=forms.CharField(widget=forms.PasswordInput(), label="Contraseña")

viviendas=(
    ('1','Casa Patio Grande'),
    ('2','Casa Patio Pequeño'),
)

regiones=(
    ('1','Región Metropolitana'),
    ('2','IV Región'),
)

ciudades=(
    ('1', 'Santiago'),
)

class Registro(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'id':'usuario'}), max_length=30, min_length=3)
    password=forms.CharField(widget=forms.PasswordInput(), max_length=20,)
    password2=forms.CharField(widget=forms.PasswordInput(), max_length=20)
    correo=forms.EmailField(widget=forms.EmailInput(), max_length=50)
    rut=forms.CharField(widget=forms.TextInput(attrs={'id':'rut'}), max_length=12)
    nombre=forms.CharField(widget=forms.TextInput(attrs={'id':'nombre'}), max_length=50)
    fechaNac=forms.DateField(widget=forms.SelectDateWidget(attrs={'id':'fecha','class':'fecha'},years=range(2018, 1939,-1)))
    telContacto=forms.CharField(widget=forms.TextInput, max_length=8)
    region=forms.ChoiceField(choices=regiones)
    ciudad=forms.ChoiceField(choices=ciudades)
    tipoVivienda=forms.ChoiceField(choices=viviendas)

#def clean_username(self):
    #username = self.cleaned_data['username']
    #if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
       # raise forms.ValidationError(u'username "%s" ya se encuentra registrado.' % username)
    #return username

def clean_password_validation(self):
        if self.cleaned_data['password'] == self.cleaned_data['password2']:
            return self.cleaned_data['password2']
        else:
            raise forms.ValidationError('Las contraseñas no coinciden')

class RegistroMascota(forms.ModelForm):
    class Meta: 
        model = Mascota
        fields= ['idMascota', 'imgMascota', 'nombreMascota', 'raza', 'descripcion', 'estado']

