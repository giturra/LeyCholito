from django.db import models


class Animal(models.Model):
    F = 'female'
    M = 'male'
    NULL = 'indeterminate'
    SEX_CHOICES = (
        (F, 'Hembra'),
        (M, 'Macho'),
        (NULL, 'Desconocido')
    )

    name = models.CharField(max_length=20)
    sex = models.CharField(max_length=20, choices=SEX_CHOICES, default=NULL)
    estimated_age = models.IntegerField(default=0)
