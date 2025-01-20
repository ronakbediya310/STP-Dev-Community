from django.contrib import admin
from .models import Doubt, Comment


@admin.register(Doubt)
class DoubtAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at")
    search_fields = ("title", "description")
    list_filter = ("created_at",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "doubt", "created_at")
    search_fields = ("content",)
    list_filter = ("created_at",)
