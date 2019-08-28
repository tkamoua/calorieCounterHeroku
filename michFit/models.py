from django.db import models
from . import calorieCounter

# Create your models here.
class ItemManager(models.Manager):
    def create_item(self,name,calories,protein):
        item = self.create(name=name, calories = calories, protein=protein)
        return item

class MenuItem(models.Model):
    name = models.CharField(max_length = 200)
    calories = models.IntegerField()
    protein = models.CharField(max_length=10)
    objects=ItemManager()





