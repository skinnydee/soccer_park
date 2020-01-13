from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    First_Name = forms.CharField(max_length=255, required=True)
    Last_Name = forms.CharField(max_length=255, required=True)
    age = forms.IntegerField(max_value=16, required=True)
    email = forms.EmailField()
 

    class Meta:
        model = User
        fields = (
                    'First_Name',
                    'Last_Name',
                    'age',
                    'username',
                    'email',
                    'password1',
                    'password2',
                 )
    
    def save(self, commit = True):
        user = super(UserRegisterForm, self).save(commit = False)
        user.first_name = self.cleaned_data['First_Name']
        user.last_name = self.cleaned_data['Last_Name']
        user.age= self.cleaned_data['age']
        user.emal = self.cleaned_data['email']

        if commit:
            user.save()