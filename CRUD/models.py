from django.db import models

# Create your models here.
class Employees(models.Model):
    name  = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    phone = models.IntegerField(max_length=50)