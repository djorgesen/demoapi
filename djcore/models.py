from django.db import models
from datetime import date, datetime
from django.contrib.auth.hashers import (check_password, make_password, is_password_usable)

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=254,unique=True)
    first_name = models.CharField(max_length=254,blank=True)
    last_name = models.CharField(max_length=254,blank=True)
    password = models.CharField('password', max_length=128)
    date_created = models.DateTimeField(auto_now_add=True)

    USER_LEVEL_CHOICES = ((1,'App User'),(2,'Admin'),)
    user_level = models.SmallIntegerField(default=1,choices=USER_LEVEL_CHOICES)

    def _get_username(self):
        if self.first_name + self.last_name != '':
            return self.first_name + ' ' + self.last_name
        else:
            return self.email
    username = property(_get_username)

    def __unicode__(self):
        return self.get_username()

    def get_username(self):
        if self.first_name + self.last_name != '':
            return self.first_name + ' ' + self.last_name
        else:
            return self.email

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """
        Returns a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """
        def setter(raw_password):
            self.set_password(raw_password)
            self.save(update_fields=["password"])
        return check_password(raw_password, self.password, setter)
