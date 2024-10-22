from django.urls import path
from . import views
urlpatterns = [
     path('admission/', views.create_admission, name='create_admission'),
    
]
