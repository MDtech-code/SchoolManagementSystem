from django.urls import path
from .views import Payrll
urlpatterns = [
    path('pay/', Payrll.as_view(), name='pay'),
]
