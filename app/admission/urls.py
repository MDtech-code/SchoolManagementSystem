from django.urls import path
from . import views
urlpatterns = [
    path('admission/',views.AdmissionView.as_view(),name='admission')
]
