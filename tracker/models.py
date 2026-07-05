from django.db import models


class Cube(models.Model):
    TYPE_CHOICES = [
        ('regular', 'Звичайний'),
        ('magnetic', 'Магнітний'),
        ('electric', 'Електричний'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"


class Session(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Session {self.id}"


class Solve(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='solves')
    cube = models.ForeignKey(Cube, on_delete=models.CASCADE)

    time = models.FloatField(help_text="Час збірки в секундах")
    scramble = models.CharField(max_length=100)

    def __str__(self):
        return f"Solve {self.id} - {self.time}s"