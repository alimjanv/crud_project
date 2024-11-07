from django.db import models


# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=40)
    age = models.IntegerField()

    def __str__(self):
        return self.name
