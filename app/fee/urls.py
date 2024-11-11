from django.urls import path
from . import views
urlpatterns = [

        path('generate/<int:admission_id>/', views.generate_voucher, name='generate_voucher'),
        path('view/<int:admission_id>/', views.view_voucher, name='view_voucher'),
        path('download/<int:admission_id>/', views.download_voucher, name='download_voucher'),
]
    

