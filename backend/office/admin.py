from import_export import resources, formats
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats

from office.models import Office


class OfficeResource(resources.ModelResource):
    class Meta:
        model = Office


class OfficeAdmin(ImportExportModelAdmin):
    list_display = ("id", "title", "country_id", "phone", "contact")
    list_display_links = ("id", "title")

    resource_classes = [OfficeResource]
    formats = [base_formats.XLSX]


admin.site.register(Office, OfficeAdmin)
