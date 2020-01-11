from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    fname = forms.CharField(max_length=255, required=True)
    lname = forms.CharField(max_length=255, required=True)
    age = forms.IntegerField(max_value=16, required=True)
    


    class Meta:
        model = User
        fields = ['Firts_name','username','email','password1','password2']