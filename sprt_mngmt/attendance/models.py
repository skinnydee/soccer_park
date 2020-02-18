from django.db import models
form django.contrib.auth.models import User


class AttendenceTable(models.Model):

    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="attendancestudent")
    coach = models.ForeignKey(User, on_delete=models.CASCADE, related_name="attendancecoach")
    date = models.DateField(auto_now=True, auto_now_add=True)
    isPresent = models.BooleanField(default=True)

    def __str__(self):
        return self.date