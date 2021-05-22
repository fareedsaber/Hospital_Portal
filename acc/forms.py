from django.db.models.fields.related import ForeignKey
from django.forms import fields
from django.forms.widgets import EmailInput, PasswordInput
from django import forms
from django.contrib.auth.models import  User
from .models import models, profile
from django.contrib.auth.forms import  UserCreationForm
from django.utils import timezone



class UserCreationForm(UserCreationForm):
    username = forms.CharField(label='UserName')
    first_name = forms.CharField(label=' First_Name')
    last_name = forms.CharField(label='Last_Name')
    email = forms.EmailField(label='Email')    
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password',widget=forms.PasswordInput())
        
    
    class Meta:
        
        model=User
        fields=['username','first_name','last_name','email','password1','password2']
         

class Login_Form(forms.ModelForm):
    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())  
    
    class  Meta:
       model= User       
       fields=('username','password')
       
class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(label='First_Name')
    last_name=forms.CharField(label=' Last_Name')
    email = forms.EmailField(label='Email')   
    
    class Meta:
        model = User
        fields=['first_name','last_name','email']
        
       
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model= profile
        fields=['FullName','Mobile','image','slug','Address']
        
        
        
