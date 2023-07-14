from django.db import models

# Create your models here.

class Talaba(models.Model):
    ism = models.CharField(max_length=120)
    familya = models.CharField(max_length=120)
    age = models.CharField(max_length=10)
    image = models.ImageField()
    phone = models.CharField(max_length=13)
    
    def __str__(self) -> str:
        return self.ism