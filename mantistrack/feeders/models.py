# Python imports
from datetime import datetime
from dateutil import relativedelta

# Core Django imports
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.generic import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

# Third party imports
from photologue.models import Gallery

# App-specific imports
from containers.models import Container
from notes.models import NoteData, Note


@python_2_unicode_compatible
class Feeder(NoteData):
    short_name = models.CharField(max_length=200)
    long_name = models.CharField(max_length=300)
    gallery = models.ForeignKey(Gallery, blank=True, null=True)

    @property
    def hatched(self):
        batches = self.batch_set.all()

        if batches:
            hatches = 0
            for batch in batches:
                hatches += batch.hatched
            return hatches
        else:
            return 0

    @property
    def available(self):
        fed = int(self.feeding_set.aggregate(models.Sum('total_fed'))['total_fed__sum'] or 0)
        died = int(self.batch_set.aggregate(models.Sum('num_died'))['num_died__sum'] or 0)
        return self.hatched - died - fed

    def __str__(self):
        return u"{0:s} available for feeding: {1:d}".format(self.short_name, self.available)

    def get_absolute_url(self):
        return reverse('feeders:detail-feeder', kwargs={'feeder_id': self.id})

    class Meta:
        verbose_name = 'feeder'
        verbose_name_plural = 'feeders'


@python_2_unicode_compatible
class Batch(NoteData):
    name = models.CharField(max_length=200)
    container = models.ForeignKey(Container, blank=True, null=True)
    date_received = models.DateTimeField(blank=True, null=True)
    num_pupae = models.PositiveIntegerField(blank=True, null=True)
    num_larvae = models.PositiveIntegerField(blank=True, null=True)
    num_died = models.PositiveIntegerField(blank=True, null=True)
    feeder = models.ForeignKey(Feeder)

    @property
    def hatched(self):
        hatches = self.hatch_set

        if hatches:
            return int(hatches.aggregate(models.Sum('num_hatched'))['num_hatched__sum'] or 0)
        else:
            return 0

    @property
    def age(self):
        age = relativedelta.relativedelta(datetime.now(self.date_received.tzinfo), self.date_received)

        if age.years > 1:
            return "{0:d} years {1:d} months and {2:d} days".format(age.years, age.months, age.days)
        elif age.years > 0:
            return "{0:d} year {1:d} months and {2:d} days".format(age.years, age.months, age.days)
        elif age.months > 1:
            return "{0:d} months and {1:d} days".format(age.months, age.days)
        elif age.months > 0:
            return "{0:d} month and {1:d} days".format(age.months, age.days)
        elif age.days > 0:
            return "{0:d} days".format(age.days)
        else:
            return 0

    def __str__(self):
        return "{0:s} {1:s}".format(self.name, self.age)

    def get_absolute_url(self):
        return reverse('feeders:detail-batch', kwargs={'feeder_id': self.feeder.id, 'batch_id': self.id})

    class Meta:
        verbose_name = 'batch'
        verbose_name_plural = 'batches'


@python_2_unicode_compatible
class Hatch(NoteData):
    date = models.DateTimeField()
    hatched_from = models.ForeignKey(Batch)
    num_hatched = models.PositiveIntegerField()

    def __str__(self):
        return "{0:d} on {1:s} from {2:s}".format(self.num_hatched, str(self.date), self.hatched_from.name)

    class Meta:
        verbose_name = 'hatch'
        verbose_name_plural = 'hatches'


@python_2_unicode_compatible
class Feeding(NoteData):
    feeder = models.ForeignKey(Feeder)
    accepted = models.PositiveSmallIntegerField()
    total_fed = models.PositiveSmallIntegerField()
    feeding_date = models.DateTimeField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self):
        return u"{0:s} {1:s}".format(self.feeder, self.feeding_date)

    def get_absolute_url(self):
        return reverse('feeders:detail-feeding', kwargs={'feeding_id': self.id})