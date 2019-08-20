from django.contrib import admin

# Register your models here.

from .models import Game, Entry

admin.site.register(Game)
admin.site.register(Entry)
