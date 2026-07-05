from django.db import models

class Cube(models.Model):
    TYPE_OF_CUBE = [
        (0, 'Regular'),
        (1, 'Magnetic'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=TYPE_OF_CUBE)

class Solve:
    time = models.DateTimeField()
    scramble = models.CharField(max_length=100)
    cube = models.ForeignKey(Cube, on_delete=models.CASCADE)

