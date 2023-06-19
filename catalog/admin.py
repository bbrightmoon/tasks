from django.contrib import admin

from catalog import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'amount',
                    'price',
                    'discount',
                    'created']
    search_fields = ['id', 'title']
    list_filter = ['category',
                   'created',
                   'updated',
                   'discount']
    list_editable = ['discount', 'amount']
    list_per_page = 10


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']
    search_fields = ['name']
    list_per_page = 10





























