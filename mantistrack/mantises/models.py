# Python imports
from datetime import datetime
from dateutil import relativedelta

# Core Django imports
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist

# Third party imports
from photologue.models import Gallery, Photo

# App-specific imports
from containers.models import Container


class UserData(models.Model):
    user = models.ForeignKey(User, editable=False)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class Breed(UserData):
    picture = models.ForeignKey(Photo, blank=True, null=True)
    short_name = models.CharField(max_length=200, unique=True)
    long_name = models.CharField(max_length=300, unique=True)
    life_expectancy = models.DecimalField(max_digits=5, decimal_places=4)
    low_temperature = models.DecimalField(max_digits=5, decimal_places=2)
    high_temperature = models.DecimalField(max_digits=5, decimal_places=2)
    low_humidity = models.DecimalField(max_digits=5, decimal_places=2)
    high_humidity = models.DecimalField(max_digits=5, decimal_places=2)
    adult_instar_male = models.SmallIntegerField()
    adult_instar_female = models.SmallIntegerField()

    def __str__(self):
        return self.short_name

    def get_absolute_url(self):
        return reverse('mantises:detail-breed', kwargs={'breed_id': self.id})

    def breed_pic(self):
        return self.picture.get_thumbnail_url()


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
class NymphColony(UserData):
    name = models.CharField(max_length=200)
    num_hatched = models.IntegerField(blank=True, null=True)
    num_died = models.IntegerField(blank=True, null=True)
    container = models.ForeignKey(Container, blank=True, null=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Mantis(UserData):
    name = models.CharField(max_length=200)
    breed = models.ForeignKey(Breed)
    born = models.DateTimeField()
    died = models.DateTimeField(blank=True, null=True)
    gallery = models.ForeignKey(Gallery, blank=True, null=True)
    container = models.ForeignKey(Container, blank=True, null=True)
    from_colony = models.ForeignKey(NymphColony, blank=True, null=True)

    VALUES = (
        ('0', 'Unknown'),
        ('1', 'Male'),
        ('2', 'Female'),
    )
    sex = models.CharField(max_length=1, choices=VALUES)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def age(self):
        died_on = ""

        if self.died:
            age = relativedelta.relativedelta(self.died - self.born)
            died_on = "Died on {0} at ".format(self.died)
        else:
            age = relativedelta.relativedelta(datetime.now(self.born.tzinfo), self.born)

        if age.years > 1:
            return "{0}{1:d} years {2:d} months and {3:d} days old".format(died_on, age.years, age.months, age.days)
        elif age.years > 0:
            return "{0}{1:d} year {2:d} months and {3:d} days old".format(died_on, age.years, age.months, age.days)
        elif age.months > 1:
            return "{0}{1:d} months and {2:d} days old".format(died_on, age.months, age.days)
        elif age.months > 0:
            return "{0}{1:d} month and {2:d} days old".format(died_on, age.months, age.days)
        elif age.days > 0:
            return "{0}{1:d} days old".format(died_on, age.days)
        else:
            return 0

    def instar(self):
        try:
            latest_molt = self.molt_set.latest('date').to_instar
        except ObjectDoesNotExist as e:
            latest_molt = 0

        return latest_molt

    def profile_pic(self):
        photos = self.gallery.public()
        return photos.filter().latest().get_thumbnail_url()

    def get_absolute_url(self):
        return reverse('mantises:detail-mantis', kwargs={'mantis_id': self.id})

    @property
    def is_adult(self):
        if (self.breed.adult_instar_male == self.instar() and self.get_sex_display() == 'Male') or \
                (self.breed.adult_instar_female == self.instar() and self.get_sex_display() == 'Female'):
            return True
        else:
            return False

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

    class Meta:
        unique_together = ('to_instar', 'from_instar', 'mantis')

    def __str__(self):
        return u"Mantis {0:s} from {1:n} to {2:n} on {3:s}"\
            .format(str(self.mantis), self.from_instar, self.to_instar, str(self.date))

    def get_absolute_url(self):
        return reverse('mantises:molt-history', kwargs={'mantis_id': self.mantis.id})


@python_2_unicode_compatible
class Ooth(UserData):
    picture = models.ForeignKey(Photo, blank=True, null=True)
    laid_by = models.ForeignKey(Mantis, blank=True, null=True)
    date_laid = models.DateTimeField()
    date_hatched = models.DateTimeField(blank=True, null=True)
    container = models.ForeignKey(Container, blank=True, null=True)
    nymphs = models.ForeignKey(NymphColony, blank=True, null=True)

    def __str__(self):
        return u"Laid by {0:s} on {1:s}"\
            .format(str(self.laid_by), str(self.date_laid))

    def get_absolute_url(self):
        return reverse('mantises:detail-ooth', kwargs={'mantis_id': self.laid_by.id, 'ooth_id': self.id})

    def pic(self):
        return self.picture.get_thumbnail_url()

    class Meta:
        verbose_name = 'ooth'
        verbose_name_plural = 'oothecae'