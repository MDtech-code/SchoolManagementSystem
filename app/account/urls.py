from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('verify_email/', views.SendEmailVerificationView.as_view(), name='send_email_verification'),
    path('verify_email_result/', views.EmailVerifyView.as_view(), name='verify_email'),
    path('forget_password/', views.ForgetPasswordView.as_view(), name='forget_password'),
    path('reset_password/', views.ResetPasswordView.as_view(), name='reset_password'),
]

'''
    path('profile/edit/', ProfileCreateOrUpdateView.as_view(), name='profile_edit'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('signup/',views.SignupViews.as_view(),name='signup'),
    path('send_verify_email/',views.SendEmailVerificationView.as_view(),name='SendVerifyEmail'),
    path ('verify_email/',views.EmailVerifyViews.as_view(),name='emailVerify'),
    path('login/',views.LoginViews.as_view(),name='login'),
    path('forget_password/',views.ForgetPasswordViews.as_view(),name='forgetPassword'),
    path('logout/',views.LogoutViews.as_view(),name='logout'),
    path('reset_password/',views.ResetPasswordView.as_view(),name='reset_password'),
    path('profile/', views.ProfileRetrieveView.as_view(), name='profile-retrieve'),
    path('profile/create/',views.ProfileCreateView.as_view(), name='profile-create'),
    path('profile/update/',views.ProfileUpdateView.as_view(), name='profile-update'),
    '''