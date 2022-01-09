from django.db import models

# Create your models here.
class Features(models.Model):
    feature1 = models.CharField(default="", null=True, max_length=20)
    feature2 = models.CharField(default="", null=True, max_length=20)
    hue = models.CharField(default="", null=True, max_length=20)