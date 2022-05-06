from django.contrib import admin

from .models import Space


@admin.register(Space)
class SpaceAdmin(admin.ModelAdmin):
    list_display = ["name", "type", "short_introduce"]
    list_per_page = 10
