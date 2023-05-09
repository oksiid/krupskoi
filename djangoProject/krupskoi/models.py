from django.db import models
from django.contrib.auth.models import User

class Kalitka(models.Model):
  entry_code = models.BooleanField(default=False)
  entry_name = models.CharField(max_length=50)

class Vorota(models.Model):
  entry_code = models.BooleanField(default=False)
  entry_name = models.CharField(max_length=50)



