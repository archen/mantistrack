__author__ = 'archen'

# Core Django imports

# Third party app imports
from reversion import VersionAdmin

# Local app imports


class UserVersionAdmin(VersionAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()