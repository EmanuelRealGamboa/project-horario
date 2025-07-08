from django.urls import path
from .views import LoginView, RegisterStudentView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterStudentView.as_view(), name='register-student'),
]
