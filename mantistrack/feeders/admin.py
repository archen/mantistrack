# Core Django imports
from django.contrib import admin

# Third party app imports

# Local app imports
from feeders.models import Feeder, Feeding, Hatch, Batch
from utils.adminwrappers import UserVersionAdmin


class FeederAdmin(UserVersionAdmin):
    list_display = ('__str__',)


class FeedingAdmin(UserVersionAdmin):
    list_display = ('__str__',)


class HatchAdmin(UserVersionAdmin):
    list_display = ('__str__',)


class BatchAdmin(UserVersionAdmin):
    list_display = ('__str__',)

admin.site.register(Feeding, FeedingAdmin)
admin.site.register(Feeder, FeederAdmin)
admin.site.register(Hatch, HatchAdmin)
admin.site.register(Batch, BatchAdmin)
