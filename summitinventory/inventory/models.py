from pydoc import describe
from django.db import models

# Create your models here.
class Inventory(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    # def set(self, field, value):
        