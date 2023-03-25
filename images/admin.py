from django.contrib import admin
from .models import Images
# Register your models here.

@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug','image','created']
    list_filter = ['created']

    