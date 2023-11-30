from django.contrib import admin
from airports.models import Airport


class AirportAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [f.name for f in self.model._meta.fields]


admin.site.register(Airport, AirportAdmin)
