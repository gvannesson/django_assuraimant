from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weight=models.PositiveIntegerField(verbose_name='poids', validators=[MinValueValidator(0), MaxValueValidator(800)])
    age=models.PositiveIntegerField(verbose_name='age',  validators=[MinValueValidator(18), MaxValueValidator(124)])
    height=models.PositiveIntegerField(verbose_name='taille', validators=[MinValueValidator(50), MaxValueValidator(250)])
    region=models.CharField(verbose_name='région',max_length=100)
    smoker=models.BooleanField(verbose_name='fumeur')
    sex=models.BooleanField(verbose_name='sexe')
    children=models.PositiveIntegerField(verbose_name="nombre d'enfants", validators=[MinValueValidator(0), MaxValueValidator(20)])
    last_charge_prediction=models.FloatField(verbose_name="dernière prédiction", round=2)

# Create your models here.
