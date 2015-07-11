from django import forms
from django.forms import ModelForm
from models import *

class UsuarioForm(ModelForm):
	class Meta:
		model = Usuario
		exclude = ("id_user", "id_rol", "fe_create", "status",)
		widgets = {'clave': forms.PasswordInput()}