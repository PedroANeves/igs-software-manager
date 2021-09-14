from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=256) # maximum email length
    departament = models.CharField(max_length=30)

    def __str__(self):
        return  f"{self.name}, {self.departament} ({self.email})"
