from django.urls import path, include  # Import include
from . import views
from django.urls import path,reverse_lazy
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [
 
]


'''
    path('', include([  # Use include to nest URLs
        path('', views.LoginView.as_view(), name='login'),
        path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
        path('signup/', views.SignupView.as_view(), name='signup'),
        


   
        # ... other account app URLs ...
    ])),
    path('verify_email/', SendEmailVerificationView.as_view(), name='send_email_verification'),
    path('verify_email_result/', EmailVerifyView.as_view(), name='verify_email'),
    path('forget_password/', ForgetPasswordView.as_view(), name='forget_password'),
    path('reset_password/', ResetPasswordView.as_view(), name='reset_password'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', EditProfileView.as_view(), name='edit_profile'),
    path('dashboard/', redirect_to_dashboard, name='redirect_to_dashboard'),
    path('home/', views.home, name='home'),
    path('student/',student_dashboard, name='student_dashboard'),
    path('teacher/',teacher_dashboard, name='teacher_dashboard'),
    path('staff/',  staff_dashboard, name='staff_dashboard'),
    '''