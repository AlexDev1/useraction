from django.db import models

# Create your models here.
class UserAction(models.Model):
    email = models.EmailField('Email')
    ip = models.GenericIPAddressField('IP')
    country_code = models.CharField("Код страны", max_length=2)
    timestamp = models.DateTimeField('Дата и время')