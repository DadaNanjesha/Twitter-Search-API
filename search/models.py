# Author : Dada Nanjesha GS (dadananjesha@rymec.com)
# Year : 2021
# Copyright: Dada Nanjesha GS

from django.db import models


class TwitterData(models.Model):
    id = models.PositiveIntegerField(primary_key=True, blank=False, unique=True)
    text = models.CharField(max_length=4000, blank=False)
    user = models.CharField(max_length=100, blank=False)
    lang = models.CharField(max_length=10, blank=False)
    url = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(null=False)
    retweet_count = models.CharField(max_length=10, default=0)
    favorite_count = models.CharField(max_length=10, default=0)

    def __str__(self):
        return f"{self.id}, {self.user}"
