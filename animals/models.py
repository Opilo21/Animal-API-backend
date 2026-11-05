from django.db import models

# Create your models here.

class Animal(models.Model):
    name = models.CharField(max_length=100)
    fact = models.TextField()
    habitat = models.CharField(max_length=100, blank=True)
    images = models.ImageField(upload_to = 'images/',blank=True, null=True)

    def __str__(self):
        return self.name
