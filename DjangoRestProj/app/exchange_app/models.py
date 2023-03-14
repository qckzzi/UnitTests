from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    firstname = models.CharField(max_length=255, verbose_name="Имя")
    secondname = models.CharField(max_length=255, verbose_name="Фамилия")
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)

    def __str__(self):
        return self.secondname

    class Meta:
        verbose_name = 'Учетная запись'
        verbose_name_plural = 'Учётные записи'
        ordering = ['secondname']


class Car(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    vin = models.CharField(max_length=255, verbose_name="ВИН-код")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


