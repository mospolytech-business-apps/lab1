from rest_framework.routers import DefaultRouter
from authentication.views import UserViewset
from schedules.views import  ScheduleViewset
from amenities.views import  AmenityViewset
from amenity_tickets.views import  AmenityTicketViewset
from amenity_cabin_types.views import  AmenityCabinTypeViewset
from routes.views import RouteViewset 
import sqlite3

router=DefaultRouter()


router.register('auth', UserViewset )
router.register('shedules',  ScheduleViewset )
router.register('amenities',  AmenityViewset )
router.register('amenities_ticket',  AmenityTicketViewset )
router.register('amenities_cabin_types',  AmenityCabinTypeViewset )
router.register('routes',  RouteViewset  )