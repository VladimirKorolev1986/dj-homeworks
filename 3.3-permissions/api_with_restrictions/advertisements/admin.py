from django.contrib import admin


class AdvertisementsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'creator', 'created_at', 'updated_at']
