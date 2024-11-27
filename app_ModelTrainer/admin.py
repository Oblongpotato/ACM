from django.contrib import admin
from .models import ConfidentImage, NonConfidentImage

@admin.register(ConfidentImage)
class ConfidentImageAdmin(admin.ModelAdmin):
    list_display = ('image_name', 'image_path', 'classified_at')
    search_fields = ('image_name',)
    list_filter = ('classified_at',)

@admin.register(NonConfidentImage)
class NonConfidentImageAdmin(admin.ModelAdmin):
    list_display = ('image_name', 'image_path', 'classified_at')
    search_fields = ('image_name',)
    list_filter = ('classified_at',)
