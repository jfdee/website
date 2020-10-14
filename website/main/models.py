from django.db import models

# Create your models here.

class developer(models.Model):
    surname = models.CharField("Фамилия", max_length = 20)
    name = models.CharField("Имя", max_length = 20)
    age = models.IntegerField("Возраст")
    
    def __str__(self):
        return self.surname

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
