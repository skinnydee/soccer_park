from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CoachRegisterForm(UserCreationForm): 
    is_coach = forms.BooleanField(initial=False)
    First_Name = forms.CharField(max_length=255, required=True)
    Last_Name = forms.CharField(max_length=255, required=True)
    age = forms.IntegerField(min_value=20, required=True)
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

    def save_coach(self, commit = True):
        user = super(CoachRegisterForm, self).save(commit = False)
        user.first_name = self.cleaned_data['First_Name']
        user.last_name = self.cleaned_data['Last_Name']
        user.age= self.cleaned_data['age']
        user.emal = self.cleaned_data['email']
        user.is_staff = True

        if commit:
            user.save()