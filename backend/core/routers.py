from rest_framework.routers import DefaultRouter

from authentication.views import UserViewSet
from authentication.views import AuthenticationViewSet
from office.views import OfficeViewSet
from country.views import CountryViewSet
from schedules.views import ScheduleViewSet
from airports.views import AirportViewSet
from tickets.views import TicketViewSet
from rest_framework import routers
from collections import OrderedDict
from amenities.views import AmenityViewSet
from survey.views import SurveyView

singleViews = [
    {"route": "report", "view": SurveyView.as_view(), "name": "Survey report"},
]


class APIRouter(routers.DefaultRouter):
    singleViews: list

    def __init__(self, singleViews: list, *args, **kwargs):
        self.singleViews = singleViews
        super().__init__(*args, **kwargs)

    def get_api_root_view(self, api_urls=None):
        """
        Return a basic root view.
        """
        api_root_dict = OrderedDict()
        list_name = self.routes[0].name
        for prefix, viewset, basename in self.registry:
            api_root_dict[prefix] = list_name.format(basename=basename)
        for singleView in self.singleViews:
            api_root_dict[singleView["route"]] = singleView["name"]
        return self.APIRootView.as_view(api_root_dict=api_root_dict)


router = APIRouter(singleViews=singleViews)

router.register("auth", AuthenticationViewSet, basename="auth")
router.register("users", UserViewSet)
router.register("offices", OfficeViewSet)
router.register("countries", CountryViewSet)
router.register("schedules", ScheduleViewSet)
router.register("amenities", AmenityViewSet)
router.register("airports", AirportViewSet)
router.register("tickets", TicketViewSet)
