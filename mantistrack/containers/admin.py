# Core Django imports
from django.contrib import admin

# Third party imports
from reversion import VersionAdmin

# App-specific imports
from containers.models import Container, ContainerType, EnvironmentReading


class ContainerAdmin(VersionAdmin):
    list_display = ('__str__',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


class ContainerTypeAdmin(VersionAdmin):
    list_display = ('__str__',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


class EnvironmentReadingAdmin(VersionAdmin):
    list_display = ('__str__',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(Container, ContainerAdmin)
admin.site.register(ContainerType, ContainerTypeAdmin)
admin.site.register(EnvironmentReading, EnvironmentReadingAdmin)