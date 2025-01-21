from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    weight=models.PositiveIntegerField(verbose_name='poids', validators=[MinValueValidator(0), MaxValueValidator(800)], default=0)
    age=models.PositiveIntegerField(verbose_name='age',  validators=[MinValueValidator(18), MaxValueValidator(124)], default=0)
    height=models.PositiveIntegerField(verbose_name='taille', validators=[MinValueValidator(50), MaxValueValidator(250)], default=50)
    region=models.CharField(verbose_name='région',choices=[(1,'northeast'),(2,'northwest'),(3,'southeast'),(4,'southwest')],max_length=100, default=1)
    smoker=models.BooleanField(verbose_name='fumeur', default=0)
    sex=models.BooleanField(verbose_name='sexe', default=1)
    children=models.PositiveIntegerField(verbose_name="nombre d'enfants", validators=[MinValueValidator(0), MaxValueValidator(20)], default=0)
    last_charge_prediction=models.FloatField(verbose_name="dernière prédiction", default=0)
    is_client=models.BooleanField(verbose_name='client', default=0)
    is_broker=models.BooleanField(verbose_name='courtier', default=0)

# Create your models here.
