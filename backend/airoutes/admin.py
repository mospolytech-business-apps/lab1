from import_export import resources, formats
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats

from airoutes.models import Route


class RouteResource(resources.ModelResource):
    class Meta:
        model = Route


class RouteAdmin(ImportExportModelAdmin):
    list_display = ("id", "DepartureAirport", "ArrivalAirport", "Distance", "FlightTime")
    list_display_links = ("id", "DepartureAirport", "ArrivalAirport")

    resource_classes = [RouteResource]
    formats = [base_formats.XLSX]


admin.site.register(Route, RouteAdmin)
