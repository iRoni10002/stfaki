from django.db import models


class Rooms(models.Model):
    name = models.CharField(max_length=50)
    rules = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name


class RoomEntry(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    color = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    
    room = models.ForeignKey('Rooms', on_delete=models.PROTECT, related_name='entries')
    user = models.ForeignKey('users.User', on_delete=models.PROTECT, related_name='room_entries')
