from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class address(models.Model):
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    pin=models.IntegerField(blank=True, null=True)
    Name=models.CharField(max_length=20)
    date=models.DateField()
    
    def __str__(self):
        return self.Name
    

