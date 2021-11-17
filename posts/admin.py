from django.contrib import admin
from . import models


@admin.register(models.OttType)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.posts.count()


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "number_of_people",
        "explain",
        "host",
        "OttType",
        "pending",
    )
