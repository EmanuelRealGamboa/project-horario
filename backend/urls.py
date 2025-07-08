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
        description="API for the school schedule management system",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@schoolapi.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
  
    path('admin/', admin.site.urls),

    path('api/institutions/', include('institutions.urls')),
    path('api/users/', include('users.urls')),  
    path('api/schedules/', include('schedules.urls')),
    path('api/conflicts/', include('conflicts.urls')),
    path('api/notifications/', include('notifications.urls')),

  
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

   
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
