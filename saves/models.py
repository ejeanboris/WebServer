from django.db import models

# Create your models here.

class Picture(models.Model):
    location = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Address(models.Model):
    Picture = models.ForeignKey(Picture, on_delete=models.CASCADE)
    value = models.CharField(max_length=200)
    importance = models.IntegerField(default=1)
