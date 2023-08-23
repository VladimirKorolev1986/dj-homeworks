from django.contrib import admin

from advertisements.models import Advertisement


@admin.register(Advertisement)
class AdvertisementsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'creator', 'created_at', 'updated_at', 'status']
