# Core Django imports
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


class UserData(models.Model):
    user = models.ForeignKey(User, editable=False)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class Breed(UserData):
    short_name = models.CharField(max_length=200)
    long_name = models.CharField(max_length=300)
    life_expectancy = models.DecimalField(max_digits=5, decimal_places=4)
    low_temperature = models.DecimalField(max_digits=5, decimal_places=2)
    high_temperature = models.DecimalField(max_digits=5, decimal_places=2)
    low_humidity = models.DecimalField(max_digits=5, decimal_places=2)
    high_humidity = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.short_name


@python_2_unicode_compatible
class Prey(UserData):
    short_name = models.CharField(max_length=200)
    long_name = models.CharField(max_length=300)
    VALUES = (
        ('0', 'In Stock'),
        ('1', 'Pupating'),
        ('2', 'Out of Stock')
    )
    status = models.CharField(max_length=1, choices=VALUES)

    def __str__(self):
        return u"{0:s} {1:s}".format(self.short_name, self.get_status_display())

    class Meta:
        verbose_name = 'prey'
        verbose_name_plural = 'prey'


@python_2_unicode_compatible
class Mantis(UserData):
    name = models.CharField(max_length=200)
    instar = models.PositiveSmallIntegerField()
    breed = models.ForeignKey(Breed)
    born = models.DateTimeField()
    died = models.DateTimeField(blank=True, null=True)
    VALUES = (
        ('0', 'Unknown'),
        ('1', 'Male'),
        ('2', 'Female'),
    )
    sex = models.CharField(max_length=1, choices=VALUES)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'mantis'
        verbose_name_plural = 'mantises'


@python_2_unicode_compatible
class Feeding(UserData):
    prey = models.ForeignKey(Prey)
    accepted = models.PositiveSmallIntegerField()
    total_fed = models.PositiveSmallIntegerField()
    feeding_date = models.DateTimeField()

    def __str__(self):
        return u"{0:s} {1:s}".format(self.prey, self.feeding_date)


@python_2_unicode_compatible
class Molt(UserData):
    mantis = models.ForeignKey(Mantis)
    date = models.DateTimeField()
    from_instar = models.PositiveSmallIntegerField()
    to_instar = models.PositiveSmallIntegerField()

    def __str__(self):
        return u"Mantis {0:s} from {1:n} to {2:n} on {3:s}"\
            .format(str(self.mantis), self.from_instar, self.to_instar, str(self.date))
