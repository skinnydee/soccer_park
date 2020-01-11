from django.db import models

class Users(models.Model):
    email = models.EmailField()
    fname = models.CharField(max_length=255, required=True)
    lname = models.CharField(max_length=255, required=True)
    age = models.IntegerField(max_value=16, required=True)