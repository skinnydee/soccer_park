from django.db import models

# Create your models here.
class Player_attendance(models.Model):
    player = models.BooleanField()