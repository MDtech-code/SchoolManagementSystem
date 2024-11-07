
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Employee
from .forms import EmployeeForm
from django.core.paginator import Paginator
from .models import StaffPerformance, Qualification
from .forms import StaffPerformanceForm, QualificationForm
from .models import EmployeeDesignation
from app.account.decorators import role_required
from django.utils.decorators import method_decorator

# List all employees
@method_decorator(role_required(['staff']), name='dispatch')
class EmployeeList(ListView):
    
    model = Employee
    template_name = '/employee_list.html'  # Specify the template name
    context_object_name = 'employees'     # Name to be used in the template for employees list
    #paginate_by=10 # Number of records per page

     # Add search functionality
    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return Employee.objects.filter(employee_name__icontains=query)
        return Employee.objects.all()

# Create a new employee
@method_decorator(role_required(['staff']), name='dispatch')
class EmployeeCreate(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee/employee_forms.html'  # Specify the template for creating a new employee
    success_url = reverse_lazy('employee_list')  # After a successful creation, redirect to employee list

# View details of an employee
@method_decorator(role_required(['staff']), name='dispatch')
class EmployeeDetail(DetailView):
    model = Employee
    template_name = 'employee/employee_detail.html'  # Specify the template for employee details
    context_object_name = 'employee'  # Name to be used in the template for the employee

# Update an existing employee
@method_decorator(role_required(['staff']), name='dispatch')
class EmployeeUpdate(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee/employee_forms.html'  # Reuse the form template for updating
    success_url = reverse_lazy('employee_list')  # Redirect to employee list after update

# Delete an employee
@method_decorator(role_required(['staff']), name='dispatch')
class EmployeeDelete(DeleteView):
    model = Employee
    template_name = 'employee/employee_confirm_delete.html'  # Specify the template for confirming delete
    success_url = reverse_lazy('employee_list')  # Redirect to employee list after deletion

# StaffPerformance Views
@method_decorator(role_required(['staff']), name='dispatch')
class StaffPerformanceList(ListView):
    model = StaffPerformance
    template_name = 'employee/staffperformance/staffperformance_list.html'
@method_decorator(role_required(['staff']), name='dispatch')
class StaffPerformanceDetail(DetailView):
    model = StaffPerformance
    template_name = 'employee/staffperformance/staffperformance_detail.html'
@method_decorator(role_required(['staff']), name='dispatch')
class StaffPerformanceCreate(CreateView):
    model = StaffPerformance
    form_class = StaffPerformanceForm
    template_name = 'employee/staffperformance/staffperformance_form.html'
    success_url = reverse_lazy('staffperformance_list')
@method_decorator(role_required(['staff']), name='dispatch')
class StaffPerformanceUpdate(UpdateView):
    model = StaffPerformance
    form_class = StaffPerformanceForm
    template_name = 'employee/staffperformance/staffperformance_form.html'
    success_url = reverse_lazy('staffperformance_list')
@method_decorator(role_required(['staff']), name='dispatch')
class StaffPerformanceDelete(DeleteView):
    model = StaffPerformance
    template_name = 'employee/staffperformance/staffperformance_confirm_delete.html'
    success_url = reverse_lazy('staffperformance_list')

# Qualification Views
@method_decorator(role_required(['staff']), name='dispatch')
class QualificationList(ListView):
    model = Qualification
    template_name = 'employee/qualification/qualification_list.html'
@method_decorator(role_required(['staff']), name='dispatch')
class QualificationDetail(DetailView):
    model = Qualification
    template_name = 'employee/qualification/qualification_detail.html'
@method_decorator(role_required(['staff']), name='dispatch')
class QualificationCreate(CreateView):
    model = Qualification
    form_class = QualificationForm
    template_name = 'employee/qualification/qualification_form.html'
    success_url = reverse_lazy('qualification_list')
@method_decorator(role_required(['staff']), name='dispatch')
class QualificationUpdate(UpdateView):
    model = Qualification
    form_class = QualificationForm
    template_name = 'employee/qualification/qualification_form.html'
    success_url = reverse_lazy('qualification_list')
@method_decorator(role_required(['staff']), name='dispatch')
class QualificationDelete(DeleteView):
    model = Qualification
    template_name = 'employee/qualification/qualification_confirm_delete.html'
    success_url = reverse_lazy('qualification_list')

#employee designation
@method_decorator(role_required(['staff']), name='dispatch')
class EmployeeDesignationList(ListView):
    model = EmployeeDesignation
    template_name = 'employee/employeedesignation/employee_designation_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("search")
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | Q(department__icontains=query)
            )
        return queryset
@method_decorator(role_required(['staff']), name='dispatch')
class EmployeeDesignationDetail(DetailView):
    model = EmployeeDesignation
    template_name = 'employee/employeedesignation/employee_designation_detail.html'
@method_decorator(role_required(['staff']), name='dispatch')
class EmployeeDesignationCreate(CreateView):
    model = EmployeeDesignation
    fields = ['name', 'department', 'description']
    template_name = 'employee/employeedesignation/employee_designation_form.html'
    success_url = reverse_lazy('employee_designation_list')
@method_decorator(role_required(['staff']), name='dispatch')
class EmployeeDesignationUpdate(UpdateView):
    model = EmployeeDesignation
    fields = ['name', 'department', 'description']
    template_name = 'employee/employeedesignation/employee_designation_form.html'
    success_url = reverse_lazy('employee_designation_list')
@method_decorator(role_required(['staff']), name='dispatch')
class EmployeeDesignationDelete(DeleteView):
    model = EmployeeDesignation
    template_name = 'employee/employeedesignation/employee_designation_confirm_delete.html'
    success_url = reverse_lazy('employee_designation_list')