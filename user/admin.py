from django.contrib import admin
from user import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'email'
    ]
    search_fields = [
        'id'
    ]
    list_per_page = 10