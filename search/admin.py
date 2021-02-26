# Author : Dada Nanjesha GS (dadananjesha@rymec.com)
# Year : 2021
# Copyright: Dada Nanjesha GS

from django.contrib import admin
from search.models import TwitterData
from import_export.admin import ImportExportModelAdmin


class TwitterDataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("id", "user", "url", "created_at")
    list_per_page = 10
    search_fields = ("id", "user")
    list_display_links = ("id", "user")


admin.site.register(TwitterData, TwitterDataAdmin)
