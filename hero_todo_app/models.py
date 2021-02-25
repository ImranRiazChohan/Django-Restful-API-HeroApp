from django.db import models
# Create your models here.

class Hero(models.Model):
    name=models.CharField(max_length=26)
    age=models.IntegerField(blank=False)

    objects=models.Manager()

    def __str__(self):
        return self.name
