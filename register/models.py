from django.db import models
from django.utils import timezone


class Attendant(models.Model):
    first_name = models.CharField(max_length=80, blank=False)
    last_name = models.CharField(max_length=80, blank=False)
    email = models.EmailField(unique=True, blank=False)
    major = models.CharField(max_length=80, blank=True)
    university = models.CharField(max_length=80, blank=True)
    registration_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
