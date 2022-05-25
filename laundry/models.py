from django.db import models


class Laundry(models.Model):
    is_available = models.BooleanField(default=True)


class LaundryEntry(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    
    laundry = models.ForeignKey('Laundry', on_delete=models.PROTECT, related_name='entries')
    user = models.ForeignKey('users.User', on_delete=models.PROTECT, related_name='laundry_entries')
