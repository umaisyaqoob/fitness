from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Excercise(models.Model):
    excercise = models.CharField(max_length=100)
    reps = models.IntegerField()
    date_today = models.DateField(default=timezone.now)
    user_refrence = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)



class Food(models.Model):
    food = models.CharField(max_length=100)
    calories = models.IntegerField()
    date_today = models.DateField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)



class Weight(models.Model):
    weight = models.IntegerField()
    date_today = models.DateField(default=timezone.now)
    user_refrence = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


