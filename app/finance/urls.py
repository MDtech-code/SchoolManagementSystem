from django.urls import path
from . import views
urlpatterns = [
    path('finance/',views.financeview.as_view(),name='finance'),
]

