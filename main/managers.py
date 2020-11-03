from django.db import models


class DeveloperQuerySet(models.QuerySet):

    def by_surname(self, surname):
        return self.filter(surname__exact=surname)

    def by_name(self, name):
        return self.filter(name__exact=name)

    def by_age(self, age):
        return self.filter(age__gt=age)

    def get_queryset(self):
        return DeveloperQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset()

    def find_developer(self, **kwargs):
        for key, value in kwargs.items():
            if key == 'surname':
                return self.get_queryset().by_surname(value)
            if key == 'name':
                return self.get_queryset().by_name(value)
            if key == 'age':
                return self.get_queryset().by_age(value)


DeveloperManager = models.Manager.from_queryset(DeveloperQuerySet)
