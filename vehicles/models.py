from django.db import models

# Create your models here.
from django.db import models


class Vehicle(models.Model):
    CATEGORY_CHOICES = [
        ("Sedan", "Sedan"),
        ("SUV", "SUV"),
        ("Truck", "Truck"),
        ("Hatchback", "Hatchback"),
        ("Sports", "Sports"),
    ]

    make = models.CharField(max_length=100)

    model = models.CharField(max_length=100)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    quantity = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.make} {self.model}"