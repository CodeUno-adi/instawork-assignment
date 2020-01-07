from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class TeamMember(models.Model):

    class Roles(models.TextChoices):
        ADMIN = 'admin'
        REGULAR = 'regular'

    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 50)
    phone_no = PhoneNumberField()
    email = models.EmailField(unique = True)
    role = models.CharField(
        max_length = 7,
        choices = Roles.choices
    )
