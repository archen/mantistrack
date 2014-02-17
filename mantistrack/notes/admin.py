# Core Django imports
from django.contrib import admin

# Third party app imports

# Local app imports
from notes.models import Note
from utils.adminwrappers import UserVersionAdmin


class NoteAdmin(UserVersionAdmin):
    list_display = ('__str__',)

admin.site.register(Note, NoteAdmin)