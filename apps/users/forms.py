"""Users forms"""

# Django
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Local imports


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label = "Nombre", widget=forms.TextInput(attrs={'placeholder':'ejemplo: Ana Cristina'}) )
    username = forms.EmailField(max_length=150, required=True, label = "Correo", widget=forms.TextInput(
    	attrs={'placeholder':'ejemplo: usuario@email.com', 'type':'email'}  ) )
    last_name = forms.CharField(max_length=30, required=True, label = "Apellido", widget=forms.TextInput(attrs={'placeholder':'Ejem. Enamorado Aguilar'}) )
    #email = forms.EmailField(max_length=254, required=True, label = "Correo", widget=forms.TextInput(attrs={'placeholder': 'Ejem. CorreoElectronico@mail.com'}))
    class Meta:
        model = User
        fields = ('username', 'first_name',
                  'last_name', 'password1', 'password2')