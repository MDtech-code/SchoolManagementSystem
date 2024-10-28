#from django.urls import path
#from .views import Emp

#urlpatterns = [
#    path('emp/', Emp.as_view(), name='emp')
#]

#from django.urls import path
#from .views import EmployeeCreate, EmployeeDetail, EmployeeUpdate, EmployeeDelete, Emp
#from . import views
#urlpatterns = [
#    # Main employee page
#    
#
#    # Employee CRUD operations
#    # path('', EmployeeList.as_view(), name='employee_list'),  # List all employees
#    path('', Emp.as_view()),
#    path('create/', EmployeeCreate.as_view(), name='employee_create'),  # Create a new employee
#    path('<int:pk>/', EmployeeDetail.as_view(), name='employee_detail'),  # View details of a single employee
#    path('<int:pk>/update/', EmployeeUpdate.as_view(), name='employee_update'),  # Update employee details
#    path('<int:pk>/delete/', EmployeeDelete.as_view(), name='employee_delete'),  # Delete an employee
#    path('empl/', views.employeedata, name='empl'),
#    path('empr/', views.employeeread, name='empr'),
#    path('empd/<int:id>/', views.empd, name='empd'),
#    path('empe/<int:id>/', views.empe, name='empe'),
#]
#

from django.urls import path
from .views import (
    EmployeeList, EmployeeCreate, EmployeeDetail, EmployeeUpdate, EmployeeDelete,
    StaffPerformanceList, StaffPerformanceDetail, StaffPerformanceCreate, StaffPerformanceUpdate, StaffPerformanceDelete,
    QualificationList, QualificationDetail, QualificationCreate, QualificationUpdate, QualificationDelete,EmployeeDesignationList, EmployeeDesignationDetail, 
    EmployeeDesignationCreate, EmployeeDesignationUpdate, EmployeeDesignationDelete
)

urlpatterns = [
    # Employee URLs 
    path('employee_list/', EmployeeList.as_view(), name='employee_list'),  # List view
    path('create/', EmployeeCreate.as_view(), name='employee_create'),  # Create view
    path('<int:pk>/', EmployeeDetail.as_view(), name='employee_detail'),  # Detail view
    path('<int:pk>/update/', EmployeeUpdate.as_view(), name='employee_update'),  # Update view
    path('<int:pk>/delete/', EmployeeDelete.as_view(), name='employee_delete'),  # Delete view

    # StaffPerformance URLs
    path('staffperformance/', StaffPerformanceList.as_view(), name='staffperformance_list'),
    path('staffperformance/<int:pk>/', StaffPerformanceDetail.as_view(), name='staffperformance_detail'),
    path('staffperformance/create/', StaffPerformanceCreate.as_view(), name='staffperformance_create'),
    path('staffperformance/<int:pk>/update/', StaffPerformanceUpdate.as_view(), name='staffperformance_update'),
    path('staffperformance/<int:pk>/delete/', StaffPerformanceDelete.as_view(), name='staffperformance_delete'),

    # Qualification URLs
    path('qualification/', QualificationList.as_view(), name='qualification_list'),
    path('qualification/<int:pk>/', QualificationDetail.as_view(), name='qualification_detail'),
    path('qualification/create/', QualificationCreate.as_view(), name='qualification_create'),
    path('qualification/<int:pk>/update/', QualificationUpdate.as_view(), name='qualification_update'),
    path('qualification/<int:pk>/delete/', QualificationDelete.as_view(), name='qualification_delete'),

    #employee designation urls
    path('employee-designation/', EmployeeDesignationList.as_view(), name='employee_designation_list'),
    path('employee-designation/<int:pk>/', EmployeeDesignationDetail.as_view(), name='employee_designation_detail'),
    path('employee-designation/create/', EmployeeDesignationCreate.as_view(), name='employee_designation_create'),
    path('employee-designation/<int:pk>/update/', EmployeeDesignationUpdate.as_view(), name='employee_designation_update'),
    path('employee-designation/<int:pk>/delete/', EmployeeDesignationDelete.as_view(), name='employee_designation_delete'),
]