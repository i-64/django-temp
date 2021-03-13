from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Goal(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    duration = models.IntegerField()
    amount = models.IntegerField()

    def __str__(self):
        return self.title

class Desposit(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    timestamp = models.TimeField(auto_now=True)

    # def __str__(self):
    #     return self.goal
