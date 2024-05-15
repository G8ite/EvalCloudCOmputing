from django.contrib import admin
from .models import Image, Tag


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('original_name', 'upload_date')
    search_fields = ['original_name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']
