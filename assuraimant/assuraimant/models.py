from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom User model for insurance prediction application.

    This model extends the default Django `AbstractUser` to include additional 
    fields specific to the insurance context, such as weight, height, region,
    smoker status, sex, number of children, and more. It also tracks the last 
    insurance premium prediction and whether the user is a client or a broker.

    Attributes:
        weight (PositiveIntegerField): User's weight in kilograms (0-800).
        height (PositiveIntegerField): User's height in centimeters (50-250).
        region (IntegerField): User's home region, represented by an integer choice (1-4).
        smoker (CharField): Whether the user is a smoker ("yes" or "no").
        sex (CharField): User's sex ("female" or "male").
        children (PositiveIntegerField): Number of children the user has (0-20).
        last_charge_prediction (FloatField): The last predicted insurance premium amount.
        is_client (BooleanField): Boolean indicating whether the user is a client (True/False).
        is_broker (BooleanField): Boolean indicating whether the user is a broker (True/False).
        date_of_birth (DateField): The user's date of birth (optional).

    Methods:
        None
    """
    weight=models.PositiveIntegerField(verbose_name='weight', validators=[MinValueValidator(0), MaxValueValidator(800)], default=0)
    height=models.PositiveIntegerField(verbose_name='height', validators=[MinValueValidator(50), MaxValueValidator(250)], default=50)
    region=models.IntegerField(verbose_name='Home region',choices=[(1,'northeast'),(2,'northwest'),(3,'southeast'),(4,'southwest')], default=1)
    smoker=models.CharField(choices=[("no", "No"), ("yes", "Yes")], verbose_name='smoker', default="no", max_length=10)
    sex=models.CharField(choices=[("female", "Female"), ("male", "Male")], verbose_name='sex', default="male", max_length=10)
    children=models.PositiveIntegerField(verbose_name="number of children", validators=[MinValueValidator(0), MaxValueValidator(20)], default=0)
    last_charge_prediction=models.FloatField(verbose_name="Last prediction", default=0)
    is_client=models.BooleanField(verbose_name='client', default=1)
    is_broker=models.BooleanField(verbose_name='Broker', default=0)
    date_of_birth = models.DateField(null=True, blank=True)


class Prediction(models.Model):
    """
    Model to store insurance premium predictions for users.

    This model stores the details of each insurance premium prediction made
    for a user, including the user's personal information at the time of prediction,
    the calculated premium, and the date of the prediction.

    Attributes:
        user_id (ForeignKey): Foreign key linking the prediction to a specific user.
        weight (PositiveIntegerField): User's weight in kilograms.
        height (PositiveIntegerField): User's height in centimeters.
        region (CharField): User's region (as a string).
        smoker (CharField): User's smoking status ("yes" or "no").
        sex (CharField): User's sex ("female" or "male").
        children (PositiveIntegerField): Number of children the user has (default is 0).
        age (PositiveIntegerField): User's age in years.
        prediction (FloatField): The predicted insurance premium amount.
        prediction_date (DateField): The date when the prediction was made, set automatically.

    Methods:
        None
    """   
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

