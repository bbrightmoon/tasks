from django.contrib import admin
from django.shortcuts import render

from catalog.models import Product, Category


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

    def analytics(self, request):
        products = Product.objects.all()
        data = [x.rate for x in products]
        titles = [x.title for x in products]

        return render(request, "dashboard.html", {"titles": titles, "data": data, "title": "Product Dashboard"})

    def get_urls(self):
        urls = super().get_urls()
        from django.urls import path
        custom_urls = [path("analytics/", self.analytics), ]
        return custom_urls + urls


admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']
    search_fields = ['name']
    list_per_page = 10


admin.site.register(Category, CategoryAdmin)










































