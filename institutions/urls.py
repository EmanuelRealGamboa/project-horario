from django.urls import path, include
from rest_framework.routers import DefaultRouter
from institutions.views import InstitutionViewSet, GroupViewSet

router = DefaultRouter()
router.register(r'institutions', InstitutionViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
