from django.contrib import admin
from importcsv import models


@admin.register(models.CSVSource)
class CSVadmin(admin.ModelAdmin):
    list_display = [
        'brand',
        'manufacturer',
        'name',
        'reviews',
        'review_title',
        'reviews_username',
        'weight'
    ]
    search_fields = ['brand',
                     'name',
                     'manufacturer']
    list_per_page = 15
