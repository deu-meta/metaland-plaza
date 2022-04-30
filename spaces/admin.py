from django.contrib import admin

from .models import Spaces

# Register your models here.


@admin.register(Spaces)
class SpaceAdmin(admin.ModelAdmin):
    list_display = ["name", "type", "short_introduce"]
    list_per_page = 10
