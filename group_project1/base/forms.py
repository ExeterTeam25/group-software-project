from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

# For the upload of images taken at specific locations 
class ImageUpload(forms.ModelForm):
  
    class Meta:
        model = Photo
        fields = ['name', 'photograph']