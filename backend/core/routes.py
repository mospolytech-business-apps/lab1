from rest_framework.routers import DefaultRouter
from authentication.views import UserViewset
from schedules.views import  ScheduleViewset
import sqlite3

router=DefaultRouter()


router.register('auth', UserViewset )
router.register('shedules',  ScheduleViewset )