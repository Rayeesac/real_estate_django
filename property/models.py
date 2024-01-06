from django.db import models

class Property(models.Model):
    name = models.CharField(unique=True, max_length=255)
    address = models.TextField()
    location = models.CharField(max_length=255)
    features = models.TextField()
    image = models.ImageField(upload_to='property_images/', null=True, blank=True)


    def __str__(self):
        return self.name

type_choices = [('1BHK', '1BHK'), ('2BHK', '2BHK'), ('3BHK', '3BHK'), ('4BHK', '4BHK')]

class Unit(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    rent_cost = models.DecimalField(max_digits=10, decimal_places=2)
    unit_type = models.CharField(max_length=4, choices=type_choices)
    features = models.TextField()