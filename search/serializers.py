# Author : Dada Nanjesha GS (dadananjesha@rymec.com)
# Year : 2021
# Copyright: Dada Nanjesha GS

from rest_framework import serializers
from .models import TwitterData


class TwitterSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwitterData
        fields = ['id', 'text', 'user', 'lang', 'url', 'created_at', 'retweet_count', 'favorite_count']
