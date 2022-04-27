from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length = 256)
    house = models.CharField(max_length = 256)

    def __str__(self):
        return f"{self.name}: {self.house}"