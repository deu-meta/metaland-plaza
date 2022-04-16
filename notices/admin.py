from django.contrib import admin

# Register your models here.
from .models import Notices


@admin.register(Notices)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "notion"]
    list_per_page = 10
