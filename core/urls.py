"""
URL configuration for school_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.conf.urls import handler404,handler403,handler400,handler500
from core.utils.errors import handler404 as custom_handler404, handler403 as custom_handler403, handler400 as custom_handler400, handler500 as custom_handler500

# Reassigning default handlers to custom handlers
handler404 = custom_handler404
handler403 = custom_handler403
handler400 = custom_handler400
handler500 = custom_handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='home/', permanent=False)), 
    path('home/',include('app.account.urls')),
    path('student/',include('app.student.urls')),
    path('admission/',include('app.admission.urls')),
    path('fee/',include('app.fee.urls')),
    path('employee/',include('app.employee.urls'), name='employee'),
    path('payroll/',include('app.payroll.urls')),
    path('inventory/',include('app.inventory.urls')),
    path('finance/',include('app.finance.urls')),
    path('attendance/',include('app.attendance.urls')),
    path('assignment/',include('app.assignment.urls')),
    path('grade/',include('app.grade.urls')),
    path('resource/',include('app.resource.urls')),
    path('communication/',include('app.communication.urls')),


]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
# Serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)