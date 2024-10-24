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
from .views import EmployeeList, EmployeeCreate, EmployeeDetail, EmployeeUpdate, EmployeeDelete

urlpatterns = [
    path('', EmployeeList.as_view(), name='employee_list'),  # List view
    path('create/', EmployeeCreate.as_view(), name='employee_create'),  # Create view
    path('<int:pk>/', EmployeeDetail.as_view(), name='employee_detail'),  # Detail view
    path('<int:pk>/update/', EmployeeUpdate.as_view(), name='employee_update'),  # Update view
    path('<int:pk>/delete/', EmployeeDelete.as_view(), name='employee_delete'),  # Delete view
]
