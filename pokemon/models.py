from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

# Create your models here.


class Pokemon(models.Model):
    name = models.CharField(max_length=30)

    class PokemonType(models.TextChoices):

        WATER = 'WA'
        GRASS = 'GR'
        GHOST = 'GH'
        STEEL = 'ST'
        FAIRY = 'FA'

    type = models.CharField(
        max_length=2, choices=PokemonType.choices, default=PokemonType.WATER)
    hp = models.IntegerField(
        default=50, validators=[
            MaxValueValidator(350),
            MinValueValidator(50)
        ])
    active = models.BooleanField(default=True)
    name_fr = models.CharField(max_length=30, default='', blank=True)
    name_ar = models.CharField(max_length=30, default='', blank=True)
    name_jp = models.CharField(max_length=30, default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
