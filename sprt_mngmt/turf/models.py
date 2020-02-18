from django.db import models
from django.contrib.auth.models import User

class member(models.Model):
    name = models.CharField(("Name"), max_length=150)
    rank = models.IntegerField(("Rank"))
    position = models.CharField(("Position"), max_length=150)
