from django.db import models
from django.core.validators import MaxValueValidator

class Employees(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    phone = models.IntegerField(validators=[MaxValueValidator(9999999999)])

    def __str__(self):
        return self.name
    
