from django.urls import path
from .views import Emp

urlpatterns = [
    path('emp/', Emp.as_view(), name='emp')
]
