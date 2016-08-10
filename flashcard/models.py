from django.db import models


class Set(models.Model):
    name = models.CharField(max_length=128)
    color = models.CharField(max_length=7, default='f5f5dc')

    def __str__(self):
        return self.name


class Card(models.Model):
    set = models.ForeignKey(Set, on_delete=models.CASCADE)
    front = models.CharField(max_length=256)
    back = models.CharField(max_length=256)

    def __str__(self):
        return "(" + self.front + ", " +  self.back + ")"
