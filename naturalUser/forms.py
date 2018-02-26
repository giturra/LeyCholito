from django import forms


class RegisterNaturalUser(forms.Form):
    first_name = forms.CharField(label='Nombre: ', max_length=200)
    last_name = forms.CharField(label='Apellido: ', max_length=200)
    username = forms.CharField(label='Correo: ', max_length=200)
    password = forms.PasswordInput()
    profile_photo = forms.ImageField(label='Foto de Perfil: ')
    bio = forms.TextInput()
    birth_date = forms.DateField(label='Fecha de Nacimiento: ')