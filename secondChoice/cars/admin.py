from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.

class CarAdmin(admin.ModelAdmin):


    def thumbnail(self,object):
        if object.car_photo:
           return format_html('<img src="{}" width="40" style="border-radius:50;"/>'.format(object.car_photo.url))
        return "no Image"
    thumbnail.short_description='Car Image'
    list_display=('car_title','thumbnail','condition','price','created_date','is_featured')
    list_display_links=('car_title','thumbnail')
    search_fields = ('model','states','year','color')
    list_editable=('is_featured',)
    list_filter=('city','color')




admin.site.register(Car,CarAdmin)