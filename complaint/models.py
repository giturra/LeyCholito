from django.db import models
from animal.models import Type


class State(models.Model):
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.state


class Complaint(models.Model):
    F = 'female'
    M = 'male'
    NULL = 'indeterminate'

    SEX_CHOICES = (
        (F, 'Hembra'),
        (M, 'Macho'),
        (NULL, 'Desconocido')
    )

    S = 'YES'
    N = 'NO'

    HURT_CHOICES = (
        (S, 'sí'),
        (N, 'no')
    )

    state = models.ManyToManyField(State)
    type = models.ManyToManyField(Type)
    sex = models.CharField(max_length=20, choices=SEX_CHOICES, default=NULL)
    color = models.CharField(max_length=20, null=True)
    injured = models.CharField(max_length=2, choices=HURT_CHOICES, default=N)
    place = models.CharField(max_length=200, null=True)

