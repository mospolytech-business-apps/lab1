from django.contrib import admin
from amenities.models import Amenity, AmenityCabinType, AmenityTicket


class AmenityAdmin(admin.ModelAdmin):
    list_display = ("name", "price")


class AmenityCabinTypeAdmin(admin.ModelAdmin):
    list_display = ("cabin_type", "amenity")


class AmenityTicketAdmin(admin.ModelAdmin):
    list_display = ("amenity", "ticket", "price")


admin.site.register(Amenity, AmenityAdmin)
admin.site.register(AmenityCabinType, AmenityCabinTypeAdmin)
admin.site.register(AmenityTicket, AmenityTicketAdmin)
