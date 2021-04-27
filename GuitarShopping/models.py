from django.db import models
from django.forms import ModelForm

class Guitar(models.Model):

    brand_name = models.CharField(max_length=20)
    instrument_type = models.CharField(max_length=20)
    model_choice = models.CharField(max_length=30, default='')
    price = models.IntegerField()

    objects = models.Manager()

    def __str__(self):
        return self.brand_name




