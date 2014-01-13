from django.db import models, IntegrityError
from django.contrib.auth.models import User


#todo: add constraint for user group
class UserData(models.Model):
    user = models.ForeignKey(User, editable=False)

    class Meta:
        abstract = True

class MantisData(UserData):
	name = models.CharField(max_length=200)
	instar = models.SmallIntegerField()

