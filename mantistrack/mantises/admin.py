# Core Django imports
from django.contrib import admin

# Third party app imports
from reversion import VersionAdmin

# Local app imports
from mantises.models import Mantis, Breed, Prey, Feeding, Molt


class MantisAdmin(VersionAdmin):
    list_display = ('__str__',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


class BreedAdmin(VersionAdmin):
    list_display = ('__str__', 'long_name')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


class PreyAdmin(VersionAdmin):
    list_display = ('__str__',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


class FeedingAdmin(VersionAdmin):
    list_display = ('__str__',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


class MoltAdmin(VersionAdmin):
    list_display = ('__str__',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(Mantis, MantisAdmin)
admin.site.register(Breed, BreedAdmin)
admin.site.register(Prey, PreyAdmin)
admin.site.register(Feeding, FeedingAdmin)
admin.site.register(Molt, MoltAdmin)