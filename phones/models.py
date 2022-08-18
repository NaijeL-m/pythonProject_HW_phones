from django.db import models

class Phones(models.Model):
    name = models.CharField(max_length=150)
    price = models.CharField(max_length=150)
    image = models.CharField(max_length=350)
    release_date = models.DateTimeField(max_length=150)
    lte_exist = models.CharField(max_length=150)
    slug = models.SlugField(max_length=250)
# Create your models here.
