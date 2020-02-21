from django import forms
from calendar import HTMLCalendar
from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.TimeField() 
    end_time = models.TimeField() 

class Cal(forms.ModelForm):

    class Meta:
        
        model = Event
        fields = (
            'title','description','start_time','end_time',
        )

    
    def check_overlap(fixed_start, fixed_end, new_start, new_end):
        overlap = False
        if new_start == fixed_end or new_end == fixed_start:    #edge case
            overlap = False
        elif (new_start >= fixed_start and new_start <= fixed_end) or (new_end >= fixed_start and new_end <= fixed_end): #innner limits
            overlap = True
        elif new_start <= fixed_start and new_end >= fixed_end: #outter limits
            overlap = True 
        return overlap 


    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('Ending times must after starting times')
            events = Event.objects.filter(day=self.day)
            if events.exists():
                for event in events:
                    if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
                        raise ValidationError(
                            'There is an overlap with another event: ' + str(event.day) + ', ' + str(
                                event.start_time) + '-' + str(event.end_time))         

    
    def save_student(self, commit = True):
        event = super(UserRegisterForm, self).save(commit = False)
        event.title = self.cleaned_data['Title']
        event.description = self.cleaned_data['Description']
        event.start_time= self.cleaned_data['Start_Time']
        event.end_time= self.cleaned_data['End_Time']

        if commit:
            event.save()
                        
