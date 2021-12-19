from django.db import models


# Create your models here.
class UserAction(models.Model):
    COUNTRY_CODE = (
        ('RU', "Россия"),
        ('CN', "Китай"),
        ('CA', "Канада"),
        ('IT', "Италия"),
        ('US', "Соединенные Штаты"),
        ('FR', "Франция"),
        ('SE', "Швеция"),
        ('TR', "Турция"),

    )
    email = models.EmailField('Email')
    ip = models.GenericIPAddressField('IP')
    country_code = models.CharField("Код страны", max_length=2, choices=COUNTRY_CODE)
    timestamp = models.DateTimeField('Дата и время')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
