# Python imports

# Core Django imports
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.generic import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

# App-specific imports
from utils.models import UserData


@python_2_unicode_compatible
class Note(UserData):
    date = models.DateTimeField()
    is_public = models.BooleanField(default=False)
    content = models.TextField(max_length=2000)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self):
        return "By {0:s} on {1:s}".format(self.user.username, self.date.strftime("%a %x at %X"))

    def get_absolute_url(self):
        return reverse('notes:detail-note', kwargs={'note_id': self.id})


class NoteData(UserData):
    notes = GenericRelation(Note)

    class Meta:
        abstract = True

    @property
    def content_type(self):
        return ContentType.objects.get_for_model(self)