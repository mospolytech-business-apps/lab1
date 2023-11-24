from import_export import resources, formats
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats

from schedules.models import Schedule


class ScheduleResource(resources.ModelResource):
    class Meta:
        model = Schedule


class ScheduleAdmin(ImportExportModelAdmin):
    list_display = ("id", "Date", "aircraft_name", "route_info", "Confirmed")
    list_display_links = ("id", "Date", "aircraft_name", "Confirmed")

    resource_classes = [ScheduleResource]
    formats = [base_formats.XLSX]

    def route_info(self, obj):
        return (
            str(obj.Route.DepartureAirport.IATACode)
            + " - "
            + str(obj.Route.ArrivalAirport.IATACode)
        )

    def aircraft_name(self, obj):
        return obj.Aircraft.Name


admin.site.register(Schedule, ScheduleAdmin)
