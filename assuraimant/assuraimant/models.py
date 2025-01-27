from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    weight=models.PositiveIntegerField(verbose_name='weight', validators=[MinValueValidator(0), MaxValueValidator(800)], default=0)
    height=models.PositiveIntegerField(verbose_name='height', validators=[MinValueValidator(50), MaxValueValidator(250)], default=50)
    region=models.IntegerField(verbose_name='Home region',choices=[(1,'northeast'),(2,'northwest'),(3,'southeast'),(4,'southwest')], default=1)
    smoker=models.CharField(choices=[("no", "No"), ("yes", "Yes")], verbose_name='smoker', default="no", max_length=10)
    sex=models.CharField(choices=[("female", "Female"), ("male", "Male")], verbose_name='sex', default="male", max_length=10)
    children=models.PositiveIntegerField(verbose_name="number of children", validators=[MinValueValidator(0), MaxValueValidator(20)], default=0)
    last_charge_prediction=models.FloatField(verbose_name="Last prediction", default=0)
    is_client=models.BooleanField(verbose_name='client', default=0)
    is_broker=models.BooleanField(verbose_name='Broker', default=0)
    date_of_birth = models.DateField(null=True, blank=True)


class Prediction(models.Model):
    user_id = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    weight=models.PositiveIntegerField()
    height=models.PositiveIntegerField()
    region=models.CharField(max_length=100)
    smoker=models.CharField (max_length=100)
    sex=models.CharField(max_length=100)
    children=models.PositiveIntegerField(default=0)
    age= models.PositiveIntegerField()
    prediction=  models.FloatField()
    prediction_date = models.DateField(auto_now_add=True)
# Create your models here.
