from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.AdmissionCreateView.as_view(), name='create_admission'),
    
]
