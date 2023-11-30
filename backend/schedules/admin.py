from import_export import resources, formats
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats

from schedules.models import Schedule


class ScheduleResource(resources.ModelResource):
    class Meta:
        model = Schedule


class ScheduleAdmin(ImportExportModelAdmin):
    list_display = (
        "id",
        "Date",
        "formatted_time",  # Display the formatted time
        "FlightNumber",
        "aircraft_code",
        "route_info",
        "Confirmed",
    )
    list_display_links = (
        "id",
        "Date",
        "formatted_time",
        "FlightNumber",
        "route_info",
        "aircraft_code",
        "Confirmed",
    )

    admin_order_field = "FlightNumber"

    resource_classes = [ScheduleResource]
    formats = [base_formats.XLSX]

    def formatted_time(self, obj):
        return obj.Time.strftime("%H:%M")

    def aircraft_code(self, obj):
        return obj.Aircraft.MakeModel

    def route_info(self, obj):
        return (
            str(obj.Route.DepartureAirport.IATACode)
            + " - "
            + str(obj.Route.ArrivalAirport.IATACode)
        )


admin.site.register(Schedule, ScheduleAdmin)
