from django.db import models


class User(models.Model):
    JWT = models.CharField(max_length=255)
    name = models.CharField(max_length=50, verbose_name='username')
    profilePic = models.CharField(max_length=255, verbose_name='avatar')
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    money = models.IntegerField()


    def __str__(self):
        return self.name
