from import_export import resources, formats
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats

from amenities.models import Amenity, AmenityCabinType, AmenityTicket


class AmenityResource(resources.ModelResource):
    class Meta:
        model = Amenity


class AmenityAdmin(ImportExportModelAdmin):
    list_display = ("id", "name", "price")
    list_display_links = ("id", "name")

    resource_classes = [AmenityResource]
    formats = [base_formats.XLSX]


admin.site.register(Amenity, AmenityAdmin)


class AmenityCabinTypeResource(resources.ModelResource):
    class Meta:
        model = AmenityCabinType


class AmenityCabinTypeAdmin(ImportExportModelAdmin):
    list_display = ("id", "cabin_type", "amenity")
    list_display_links = ("id", "cabin_type", "amenity")

    resource_classes = [AmenityCabinTypeResource]
    formats = [base_formats.XLSX]


admin.site.register(AmenityCabinType, AmenityCabinTypeAdmin)


class AmenityTicketResource(resources.ModelResource):
    class Meta:
        model = AmenityTicket


class AmenityTicketAdmin(ImportExportModelAdmin):
    list_display = ("id", "amenity", "ticket", "price")
    list_display_links = ("id", "amenity", "ticket")

    resource_classes = [AmenityTicketResource]
    formats = [base_formats.XLSX]


admin.site.register(AmenityTicket, AmenityTicketAdmin)
