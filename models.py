#models.py (database tables)

from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=100)
    current_amount = models.FloatField()
    vegetarian = models.BooleanField(default=True)
    staple = models.BooleanField(default=False)
    measurement_unit = models.ForeignKey('MeasurmentUnit')
    categories = models.ManyToManyField('Category')

class Purchase(models.Model):
    food = models.ForeignKey('Food')
    brand = models.ForeignKey('Brand')
    store = models.ForeignKey('Store')
    purchase_date = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    useby_date = models.DateField()
    purchase_amount = models.FloatField()
    measurement_unit = models.ForeignKey('MeasurementUnit')

class Category(models.Model):
    category = models.CharField(max_length=100)
    parent = models.ForeignKey('self')

class MeasurementUnit(models.Model):
    measurement_unit = models.CharField(max_length=45)

class Store(models.Model):
    store = models.CharField(max_length=45)

class Brand(models.Model):
    brand = models.CharField(max_length=100)
