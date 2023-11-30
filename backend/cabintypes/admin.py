from import_export import resources, formats
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats

from cabintypes.models import CabinType


class CabinTypeResource(resources.ModelResource):
    class Meta:
        model = CabinType


class CabinTypeAdmin(ImportExportModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")

    resource_classes = [CabinTypeResource]
    formats = [base_formats.XLSX]


admin.site.register(CabinType, CabinTypeAdmin)
