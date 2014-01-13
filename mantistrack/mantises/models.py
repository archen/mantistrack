# Core Django imports
from django.db import models, IntegrityError
from django.contrib.auth.models import User

# Third-party app imports
from django_extensions.db.models import TimeStampedModel


#todo: add constraint for user group
class UserData(TimeStampedModel):
    user = models.ForeignKey(User, editable=False)

    class Meta:
        abstract = True

class MantisData(UserData):
	name = models.CharField(max_length=200)
	instar = models.SmallIntegerField()

class MoltData(UserData):

