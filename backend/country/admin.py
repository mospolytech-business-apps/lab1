from import_export import resources, formats
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats

from country.models import Country


class CountryResource(resources.ModelResource):
    class Meta:
        model = Country


class CountryAdmin(ImportExportModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")

    resource_classes = [CountryResource]
    formats = [base_formats.XLSX]


admin.site.register(Country, CountryAdmin)
