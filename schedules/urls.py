from django.urls import path, include
from rest_framework.routers import DefaultRouter
from schedules.views import (
    SubjectViewSet, RoomViewSet, ScheduleViewSet, TeacherAvailabilityViewSet
)

router = DefaultRouter()
router.register(r'subjects', SubjectViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'schedules', ScheduleViewSet)
router.register(r'teacher-availability', TeacherAvailabilityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
