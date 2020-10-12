from django.db import models

# Create your models here.

class developer(models.Model):
    surname = models.CharField("Фамилия", max_length = 20)
    name = models.CharField("Имя", max_length = 20)
    age = models.IntegerField("Возраст")
    post_choises = (
        (1 , "Front-end"),
        (2 , "Back-end"),
        (3 , "Analyse"),
    )
    post_stage_choises = (
        (1, "Junior"),
        (2, "Middle"),
        (3, "Senior"),
    )
    post = models.CharField(
        max_length = 2,
        choices = post_choises,
    )

    post_stage = models.CharField(
        max_length = 2,
        choices = post_stage_choises,
    )
    def __str__(self):
        return self.surname
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
