from typing import Any
from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    date = models.DateField(auto_now_add=True)
    zipcode = models.IntegerField(max_length=10)
    phone = models.IntegerField(max_length=15)   

    def __str__(self):
        return f'{self.username} {self.email} {self.date}'
    
