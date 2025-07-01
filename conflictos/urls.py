from django.urls import path, include
from rest_framework.routers import DefaultRouter
from conflictos.views import ConflictoHorarioViewSet

router = DefaultRouter()
router.register(r'conflictos', ConflictoHorarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
