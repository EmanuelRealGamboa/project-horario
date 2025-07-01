from django.urls import path, include
from rest_framework.routers import DefaultRouter
from usuarios.views import UsuarioViewSet, ProfesorViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'profesores', ProfesorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
