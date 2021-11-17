from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class UserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        ("Info", {
            "fields": (
                "bio",
                "avatar",
                "login_method",
            ),
        }),
    )

    list_display = (
        "username",
        "email",
        "login_method",
    )
