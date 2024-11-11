from django.urls import path
from . import views
urlpatterns = [
    path('apply/', views.apply_for_admission, name='apply_for_admission'),
    #spath('initiate/', views.initiate_admission, name='initiate_admission'),
]
    #path('create/', views.AdmissionCreateView.as_view(), name='create_admission'),