from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Employee, StaffPerformance, Qualification, EmployeeDesignation
from .forms import EmployeeForm, StaffPerformanceForm, QualificationForm
from django.core.paginator import Paginator

# List all employees
class EmployeeList(ListView):
    model = Employee
    template_name = 'employee_list.html'
    context_object_name = 'employees'
    paginate_by = 10

    # Add search functionality
    def get_queryset(self):
        query = self.request.GET.get('search')
        queryset = Employee.objects.select_related('designation', 'employee_pay_structure')
        if query:
            return queryset.filter(employee_name__icontains=query)
        return queryset

# Create a new employee
class EmployeeCreate(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee_forms.html'
    success_url = reverse_lazy('employee_list')

# View details of an employee
class EmployeeDetail(DetailView):
    model = Employee
    template_name = 'employee_detail.html'
    context_object_name = 'employee'

    def get_queryset(self):
        return Employee.objects.select_related('designation', 'employee_pay_structure')

# Update an existing employee
class EmployeeUpdate(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee_forms.html'
    success_url = reverse_lazy('employee_list')

# Delete an employee
class EmployeeDelete(DeleteView):
    model = Employee
    template_name = 'employee_confirm_delete.html'
    success_url = reverse_lazy('employee_list')

# StaffPerformance Views
class StaffPerformanceList(ListView):
    model = StaffPerformance
    template_name = 'staffperformance/staffperformance_list.html'

    def get_queryset(self):
        return StaffPerformance.objects.select_related('employee__designation')

class StaffPerformanceDetail(DetailView):
    model = StaffPerformance
    template_name = 'staffperformance/staffperformance_detail.html'

    def get_queryset(self):
        return StaffPerformance.objects.select_related('employee__designation')

class StaffPerformanceCreate(CreateView):
    model = StaffPerformance
    form_class = StaffPerformanceForm
    template_name = 'staffperformance/staffperformance_form.html'
    success_url = reverse_lazy('staffperformance_list')

class StaffPerformanceUpdate(UpdateView):
    model = StaffPerformance
    form_class = StaffPerformanceForm
    template_name = 'staffperformance/staffperformance_form.html'
    success_url = reverse_lazy('staffperformance_list')

class StaffPerformanceDelete(DeleteView):
    model = StaffPerformance
    template_name = 'staffperformance/staffperformance_confirm_delete.html'
    success_url = reverse_lazy('staffperformance_list')

# Qualification Views
class QualificationList(ListView):
    model = Qualification
    template_name = 'qualification/qualification_list.html'

    def get_queryset(self):
        return Qualification.objects.select_related('employee')

class QualificationDetail(DetailView):
    model = Qualification
    template_name = 'qualification/qualification_detail.html'

    def get_queryset(self):
        return Qualification.objects.select_related('employee')

class QualificationCreate(CreateView):
    model = Qualification
    form_class = QualificationForm
    template_name = 'qualification/qualification_form.html'
    success_url = reverse_lazy('qualification_list')

class QualificationUpdate(UpdateView):
    model = Qualification
    form_class = QualificationForm
    template_name = 'qualification/qualification_form.html'
    success_url = reverse_lazy('qualification_list')

class QualificationDelete(DeleteView):
    model = Qualification
    template_name = 'qualification/qualification_confirm_delete.html'
    success_url = reverse_lazy('qualification_list')

# Employee Designation Views
class EmployeeDesignationList(ListView):
    model = EmployeeDesignation
    template_name = 'employeedesignation/employee_designation_list.html'

class EmployeeDesignationDetail(DetailView):
    model = EmployeeDesignation
    template_name = 'employeedesignation/employee_designation_detail.html'

class EmployeeDesignationCreate(CreateView):
    model = EmployeeDesignation
    fields = ['name', 'department', 'description']
    template_name = 'employeedesignation/employee_designation_form.html'
    success_url = reverse_lazy('employee_designation_list')

class EmployeeDesignationUpdate(UpdateView):
    model = EmployeeDesignation
    fields = ['name', 'department', 'description']
    template_name = 'employeedesignation/employee_designation_form.html'
    success_url = reverse_lazy('employee_designation_list')

class EmployeeDesignationDelete(DeleteView):
    model = EmployeeDesignation
    template_name = 'employeedesignation/employee_designation_confirm_delete.html'
    success_url = reverse_lazy('employee_designation_list')
