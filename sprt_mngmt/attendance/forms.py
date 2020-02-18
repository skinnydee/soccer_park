from django import forms
from django.forms import formset_factory
from .models import AttendenceTable

class AttendanceForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['isPresent'].widget.attrs.update({'class': 'textinput form-control'})
    class Meta:
        model = AttendenceTable
        fields = ['isPresent']