from django.db import models
from .enums import TypeOfCube

class Cube(models.Model):

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=TypeOfCube.choices)

class Solve:
    time = models.DateTimeField()
    scramble = models.CharField(max_length=100)
    cube = models.ForeignKey(Cube, on_delete=models.CASCADE)

