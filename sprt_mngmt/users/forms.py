from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    First_Name = forms.CharField(max_length=255, required=True)
    Last_Name = forms.CharField(max_length=255, required=True)
    age = forms.IntegerField(max_value=16, required=True)
    


    class Meta:
        model = User
        fields = ('First_Name','Last_Name','age','username','email','password1','password2',)