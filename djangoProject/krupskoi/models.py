from django.db import models
from django.contrib.auth.models import User

class Kalitka(models.Model):
  entry_code = models.BooleanField(default=False)
  entry_name = models.CharField(max_length=50)

class Vorota(models.Model):
  entry_code = models.BooleanField(default=False)
  entry_name = models.CharField(max_length=50)

class Premission(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  p_kalitka = models.BooleanField(default=False)
  p_vorota = models.BooleanField(default=False)

  def __str__(self):

    if (self.p_vorota == True):
      vorota = 'Vorota'
    else:
      vorota = ' '
    if (self.p_kalitka == True):
      kalitka = 'Kalitka'
    else:
      kalitka = ' '
    return 'Имя: ' + self.user.first_name + ',  ' +  self.user.username + ',    Кв: ' + self.user.last_name + 'Доступы:  ' + vorota +' ,  ' +kalitka


