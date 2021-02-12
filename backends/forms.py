from django import forms
from django.contrib.auth.models import User

from .models import Links, Services, Institutionals, Archives

#Users
class UserForm(forms.ModelForm):
    confirm_password = forms.CharField(label='Confirme a Senha', max_length=200)  
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'confirm_password']

class UserFormUpdate(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

#Links
class LinksForm(forms.ModelForm):      
    class Meta:
        model = Links
        fields = ('description', 'link')

#Services
class ServicesForm(forms.ModelForm):      
    class Meta:
        model = Services
        fields = ('description', 'name')

#Institucional
class InstitucionalForm(forms.ModelForm):      
    class Meta:
        model = Institutionals
        fields = ('description', 'name')

#Arquivos
class ArchiveForm(forms.ModelForm):
    class Meta:
        model = Archives
        fields = ('name', 'category', 'docfile')

