from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class InventoryUser(AbstractUser):
    username = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=100)
    permissions = models.IntegerField(default=0)
    token = models.CharField(max_length=1000, default=0)
    
    def __str__(self):
        return (f'[Username: {self.username}, Password: {self.password}, '
              + f'Permissions: {self.permissions}]')