from import_export import resources, formats
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats

from airoutes.models import Route


class RouteResource(resources.ModelResource):
    class Meta:
        model = Route


class RouteAdmin(ImportExportModelAdmin):
    list_display = (
        "id",
        "departure_airport",
        "arrival_airport",
        "Distance",
        "FlightTime",
    )
    list_display_links = (
        "id",
        "departure_airport",
        "arrival_airport",
    )

    def departure_airport(self, obj):
        return obj.DepartureAirport.IATACode

    def arrival_airport(self, obj):
        return obj.ArrivalAirport.IATACode

    resource_classes = [RouteResource]
    formats = [base_formats.XLSX]


admin.site.register(Route, RouteAdmin)
