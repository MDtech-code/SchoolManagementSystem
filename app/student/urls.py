from django.urls import path
from . import views
urlpatterns = [
     path('student/',views.student_dashboard, name='student_dashboard'),
    
]
    #path('',views.StudentView.as_view(),name='student'),
