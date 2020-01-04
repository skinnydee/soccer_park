from django.db import models
from django.contrib.auth.models import User

class member(models.Model):
    name = models.CharField(max_length=50)
    rank = models.DecimalField(max_digits=5, decimal_places=0)
    position = models.CharField(max_length=50)