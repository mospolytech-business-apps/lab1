from import_export import resources, formats
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats

from aircrafts.models import Aircraft


class AircraftResource(resources.ModelResource):
    class Meta:
        model = Aircraft


class AircraftAdmin(ImportExportModelAdmin):
    list_display = ("id", "Name", "MakeModel", "TotalSeats", "EconomySeats", "BusinessSeats")
    list_display_links = ("id", "Name", "MakeModel")

    resource_classes = [AircraftResource]
    formats = [base_formats.XLSX]


admin.site.register(Aircraft, AircraftAdmin)
