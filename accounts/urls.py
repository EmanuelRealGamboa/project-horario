from django.urls import path
from .views import StudentRegisterView, StudentLoginView, StudentLogoutView

urlpatterns = [
    path('register/', StudentRegisterView.as_view()),
    path('login/', StudentLoginView.as_view()),
    path('logout/', StudentLogoutView.as_view()),
]
