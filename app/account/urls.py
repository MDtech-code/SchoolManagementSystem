from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('verify_email/', SendEmailVerificationView.as_view(), name='send_email_verification'),
    path('verify_email_result/', EmailVerifyView.as_view(), name='verify_email'),
    path('forget_password/', ForgetPasswordView.as_view(), name='forget_password'),
    path('reset_password/', ResetPasswordView.as_view(), name='reset_password'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]

