from django.urls import path, include
from rest_framework.routers import DefaultRouter
from conflicts.views import ScheduleConflictViewSet

router = DefaultRouter()
router.register(r'conflicts', ScheduleConflictViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
