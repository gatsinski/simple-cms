from django.contrib import admin

from . import models


@admin.register(models.Page)
class PageAdmin(admin.ModelAdmin):
    list_filter = ("page_type", "created_at", "updated_at")
    list_display = ("title", "page_type", "created_at", "updated_at")
    list_per_page = 15
    search_fields = ("title", "description",)
    prepopulated_fields = {"slug": ("title",)}
