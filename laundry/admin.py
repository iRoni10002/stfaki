from django.contrib import admin
from .models import Laundry, LaundryEntry


@admin.register(Laundry)
class LaundryAdmin(admin.ModelAdmin):
    pass

@admin.register(LaundryEntry)
class LaundryEntryAdmin(admin.ModelAdmin):
    pass
