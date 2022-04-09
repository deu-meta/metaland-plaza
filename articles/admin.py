from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(Articles)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["id", "category", "title", "created_at"]


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", "article"]
