from django.db import models
from django.contrib.auth.models import User


# Create your models here.

#specifying the profile table for the database
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #displays how the profile is printed. This makes it more descriptive
    def __str__(self):
        return f'{self.user.username} Profile'
