from django.contrib import admin
from .models import Rooms, RoomEntry


@admin.register(Rooms)
class RoomsAdmin(admin.ModelAdmin):
    pass


@admin.register(RoomEntry)
class RoomEntryAdmin(admin.ModelAdmin):
    pass

