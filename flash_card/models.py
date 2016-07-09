from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Set(models.Model):
    name = models.CharField(max_length=128)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

class Card(models.Model):
    set = models.ForeignKey(Set, on_delete=models.CASCADE)
    front = models.CharField(max_length=256)
    back = models.CharField(max_length=256)

    def __str__(self):
        return "{" + self.front + ", " +  self.back + "}"