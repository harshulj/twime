from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import JSONField

from .constants import Days
from .managers import UserManager

class User(models.Model):
    user_id     = models.CharField(max_length=64, blank=True, db_index=True)
    name        = models.CharField(max_length=256, blank=True)
    username    = models.CharField(max_length=256)
    url         = models.URLField(max_length=128, blank=True)
    description = models.CharField(max_length=1024, blank=True)
    verified    = models.BooleanField(default=False, blank=True)
    tweet_count = models.PositiveIntegerField(default=0)
    time_zone   = models.CharField(max_length=128, blank=True)
    location    = models.CharField(max_length=128, blank=True, null=True)
    language    = models.CharField(max_length=16, blank=True)
    followers_count = models.PositiveIntegerField(default=0)
    following_count = models.PositiveIntegerField(default=0)
    listed_count    = models.PositiveIntegerField(default=0)
    favourites_count    = models.PositiveIntegerField(default=0)
    profile_image_url   = models.URLField(blank=True)

    raw         = JSONField(default={}, blank=True)

    account_created_on  = models.DateTimeField(blank=True)
    last_status_on  = models.DateTimeField(blank=True, null=True)
    created_on      = models.DateTimeField(auto_now_add=True)
    updated_on      = models.DateTimeField(auto_now=True)

    best_time   = models.TimeField(blank=True, null=True)
    best_day    = models.CharField(max_length=3, choices=Days.choices(), blank=True, null=True)

    followers   = models.ManyToManyField('self', blank=True)

    objects     = UserManager()


    def __unicode__(self):
        return self.username
