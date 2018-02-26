from django.db import models


class Type(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type


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
    type = models.ManyToManyField(Type)
    profile_photo = models.ImageField(null=True)
    sex = models.CharField(max_length=20, choices=SEX_CHOICES, default=NULL)
    estimated_age = models.IntegerField(default=0)
    is_adoption = models.BooleanField(default=False)
    adoption_time = models.DateField(null=True)




