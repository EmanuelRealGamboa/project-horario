from django.urls import path
from .views import SignupView, VerifyCodeView, SigninView, Confirm2FAView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('verify/', VerifyCodeView.as_view(), name='verify'),
    path('signin/', SigninView.as_view(), name='signin'),
    path('confirm/', Confirm2FAView.as_view(), name='confirm'),
]