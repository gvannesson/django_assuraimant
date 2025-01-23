from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser, BaseUserManager


# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         """Create and return a regular user."""
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         """Create and return a superuser."""
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if not extra_fields.get('is_staff'):
#             raise ValueError('Superuser must have is_staff=True.')
#         if not extra_fields.get('is_superuser'):
#             raise ValueError('Superuser must have is_superuser=True.')
#         return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    weight=models.PositiveIntegerField(verbose_name='poids', validators=[MinValueValidator(0), MaxValueValidator(800)], default=0)
    age=models.PositiveIntegerField(verbose_name='age',  validators=[MinValueValidator(18), MaxValueValidator(124)], default=0)
    height=models.PositiveIntegerField(verbose_name='taille', validators=[MinValueValidator(50), MaxValueValidator(250)], default=50)
    region=models.CharField(verbose_name='région',choices=[(1,'northeast'),(2,'northwest'),(3,'southeast'),(4,'southwest')],max_length=100, default=1)
    smoker=models.CharField(choices=[("no", "Non"), ("yes", "Oui")], verbose_name='sexe', default="no", max_length=10)
    sex=models.CharField(choices=[("female", "Femme"), ("male", "Homme")], verbose_name='sexe', default="male", max_length=10)
    children=models.PositiveIntegerField(verbose_name="nombre d'enfants", validators=[MinValueValidator(0), MaxValueValidator(20)], default=0)
    last_charge_prediction=models.FloatField(verbose_name="dernière prédiction", default=0)
    is_client=models.BooleanField(verbose_name='client', default=0)
    is_broker=models.BooleanField(verbose_name='courtier', default=0)
    # objects=UserManager()


# Create your models here.
