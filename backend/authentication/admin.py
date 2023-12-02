from django.contrib import admin
from authentication.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "first_name",
        "last_name",
        "is_new",
        "is_active",
        "birthday",
    )
    list_display_links = (
        "id",
        "email",
        "first_name",
        "last_name",
        "is_new",
        "is_active",
        "birthday",
    )
    search_fields = (
        "id",
        "email",
        "last_name",
    )
    list_filter = ("last_name", "email")


admin.site.register(User, UserAdmin)
