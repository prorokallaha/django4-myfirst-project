from statistics import mode
from django.db import models
import datetime


class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    text = models.CharField(max_length= 255)
    url = models.URLField(blank=True)


    def __str__(self):
        return self.title
