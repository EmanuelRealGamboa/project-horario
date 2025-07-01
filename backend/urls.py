from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="School Schedule API",
        default_version='v1',
        description="API para el sistema de horarios escolares",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ Incluye las rutas de tus apps reales
    path('api/instituciones/', include('instituciones.urls')),
    path('api/usuarios/', include('usuarios.urls')),
    path('api/horarios/', include('horarios.urls')),
    path('api/conflictos/', include('conflictos.urls')),
    path('api/notificaciones/', include('notificaciones.urls')),

    # JWT Auth
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
