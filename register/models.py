from django.db import models
from . import validators
from django.utils import timezone


class Attendant(models.Model):
    first_name = models.CharField(max_length=80, validators=[validators.isalphavalidator], blank=False)
    last_name = models.CharField(max_length=80, validators=[validators.isalphavalidator], blank=False)
    email = models.EmailField(unique=True)
    major = models.CharField(max_length=80)
    university = models.CharField(max_length=80)
    registration_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
