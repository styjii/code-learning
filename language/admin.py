from django.contrib import admin

from .models import PageContent


@admin.register(PageContent)
class PageContentAdmin(admin.ModelAdmin):
    list_display = ("key", "signature", "updated_at")
    search_fields = ("key",)
    readonly_fields = ("updated_at",)
