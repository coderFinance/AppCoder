from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppCoder.models import Profile


class FormCurso(forms.Form):
    grado = forms.IntegerField()
    division = forms.CharField()
    turno = forms.CharField()
    año = forms.IntegerField()
    imagen = forms.ImageField()

class FormAlumno(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.IntegerField()
    # año_nacimiento = forms.DateField()
    # domicilio_calle = forms.CharField()
    # domicilio_calleNumero = forms.IntegerField()
    # domicilio_cp = forms.IntegerField()
    # domicilio_localidad = forms.CharField()
    # provincia = forms.CharField()
    telefono_contacto = forms.IntegerField()
    imagen = forms.ImageField()


class FormDocente(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.IntegerField()
    telefono_contacto = forms.IntegerField()
    imagen = forms.ImageField()
   
     
class FormDirectivo(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.IntegerField()
    telefono_contacto = forms.IntegerField()
    imagen = forms.ImageField()



class UserEditForm(UserCreationForm):

    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Modificar email")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'email', 'password1', 'password2' ]



# class AvatarForm(forms.ModelForm):
#     class Meta:
#         model = Avatar
#         fields = ('user', 'imagen',)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido. 254 carácteres como máximo y debe ser válido.")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya está registrado, prueba con otro.")
        return email


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio']
