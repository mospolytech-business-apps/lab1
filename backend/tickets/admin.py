from import_export import resources, formats
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats

from tickets.models import Ticket


class TicketResource(resources.ModelResource):
    class Meta:
        model = Ticket


class TicketAdmin(ImportExportModelAdmin):
    list_display = (
        "id",
        "user",
        "schedule_info",
        "cabin_type",
        "first_name",
        "last_name",
        "email",
        "phone",
        "passport_number",
        "passport_country_id",
        "booking_reference",
        "confirmed",
    )
    list_display_links = ("id", "first_name", "last_name")

    resource_classes = [TicketResource]
    formats = [base_formats.XLSX]

    def user_info(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"

    def schedule_info(self, obj):
        return f"{obj.schedule.FlightNumber}, {obj.schedule.Route.DepartureAirport.IATACode} - {obj.schedule.Route.ArrivalAirport.IATACode}, {obj.schedule.Date}, {obj.schedule.Time}"

    def cabin_type_info(self, obj):
        return obj.cabin_type.name

    user_info.short_description = "User"
    schedule_info.short_description = "Schedule"
    cabin_type_info.short_description = "Cabin Type"


admin.site.register(Ticket, TicketAdmin)
