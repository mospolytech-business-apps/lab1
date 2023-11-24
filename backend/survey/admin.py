from django.contrib import admin
from survey.models import Survey
from django_admin_listfilter_dropdown.filters import (
    DropdownFilter,
    ChoiceDropdownFilter,
    RelatedDropdownFilter,
)


class SurveyAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [f.name for f in self.model._meta.fields]

    list_filter = [
        ("month", DropdownFilter),
    ]


admin.site.register(Survey, SurveyAdmin)
