from import_export import resources, formats
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats

from airports.models import Airport


class AirportResource(resources.ModelResource):
    class Meta:
        model = Airport


class AirportAdmin(ImportExportModelAdmin):
    list_display = ("id", "CountryID", "IATACode", "Name")
    list_display_links = ("id", "CountryID", "IATACode", "Name")

    resource_classes = [AirportResource]
    formats = [base_formats.XLSX]


admin.site.register(Airport, AirportAdmin)
