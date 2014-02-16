# Core Django imports
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse


class UserData(models.Model):
    user = models.ForeignKey(User, editable=False)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class ContainerType(UserData):
    name = models.CharField(max_length=200, unique=True)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    length = models.DecimalField(max_digits=5, decimal_places=2)
    width = models.DecimalField(max_digits=5, decimal_places=2)
    url = models.URLField(blank=True)
    VALUES = (
        ('0', 'Rectangular'),
        ('1', 'Cube'),
        ('2', 'Deli Cup'),
        ('3', 'Cylinder'),
        ('4', 'Hexagonal'),
        ('5', 'Round'),
    )
    type = models.CharField(max_length=1, choices=VALUES)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('containers:detail-container-type', kwargs={'container_type_id': self.id})

    class Meta:
        unique_together = (('height', 'length', 'width', 'type'),)
        verbose_name = 'container type'
        verbose_name_plural = 'container types'


@python_2_unicode_compatible
class Container(UserData):
    name = models.CharField(max_length=200)
    type = models.ForeignKey(ContainerType)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('containers:detail-container', kwargs={'container_id': self.id})

    class Meta:
        verbose_name = 'container'
        verbose_name_plural = 'containers'


@python_2_unicode_compatible
class EnvironmentReading(UserData):
    date = models.DateTimeField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    container = models.ForeignKey(Container)

    def __str__(self):
        return u"{0} temperature: {1} humidity: {2}".format(self.date, self.temperature, self.humidity)

    def get_absolute_url(self):
        return reverse('containers:reading-history', kwargs={'container_id': self.container.id})

    class Meta:
        unique_together = ('date', 'container')
        verbose_name = 'environment reading'
        verbose_name_plural = 'environment readings'