from django.db import models
from django.contrib.auth.models import User

class member(models.Model):
<<<<<<< HEAD
    name = models.CharField(("Name"), max_length=150)
    rank = models.IntegerField(("Rank"))
    position = models.CharField(("Position"), max_length=150)
=======
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
>>>>>>> master
