from django.db import models
from django.core.validators import MinValueValidator
from datetime import datetime, date
from django.utils import timezone

from numpy import mod
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f'{self.id} | {self.name}'

class MeasureUnit(models.Model):
    description = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.description

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=40)

    def __str__(self) -> str:
        return f'{self.description}'

class Buy(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    qty = models.PositiveIntegerField(default=0)
    #buy_datetime = models.DateTimeField(auto_now_add=True)
    buy_datetime = models.DateField(default=timezone.now)
    #mesaure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.id} | {self.product} | {self.buy_datetime}'
