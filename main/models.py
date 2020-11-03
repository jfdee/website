from django.db import models
from .managers import DeveloperManager


class Developer(models.Model):
    surname = models.CharField("Фамилия", max_length=20)
    name = models.CharField("Имя", max_length=20)
    age = models.IntegerField("Возраст")

    def __str__(self):
        return f"{self.surname} {self.name} {self.age}"

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    objects = DeveloperManager()
