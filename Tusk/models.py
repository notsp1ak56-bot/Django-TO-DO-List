from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class State(models.Model):
    importance = models.CharField(max_length=50, default="Неуказанно ")

    def __str__(self):
        return f"{self.importance}"

class Tusks(models.Model):
    title = models.CharField(max_length= 100 , default= "Неуказанно ")
    target = models.CharField(max_length= 500 , default= "Неуказанно")
    is_completed = models.BooleanField(default= False)
    importance = models.ForeignKey(State , on_delete= models.CASCADE , null=True, blank= True)
    owner = models.ForeignKey(User , on_delete= models.CASCADE , null=True, blank=True)

    def __str__(self):
        return f"{self.title}"
