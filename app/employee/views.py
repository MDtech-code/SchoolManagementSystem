#from django.shortcuts import render
#from django.views import View
# Create your views here.
#class Emp(View):
 #   def get(self, request):
  #      return render(request, 'employee/employee.html')
#
#from django.shortcuts import render, get_object_or_404, redirect
#from django.urls import reverse_lazy
#from django.views import View  # <-- Import the View class
#from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView  # Generic views for CRUD operations
#from .models import Employee
#from .forms import EmployeeForm
#from django.http import HttpResponseRedirect

# Class-based view for displaying a template
# class Emp(View):
#     def get(self, request):
#         return render(request, 'employee.html')

## List all employees
#class Emp(View):
#    def get(self, request):
#        emp = EmployeeForm
#        return render(request, "employee_list.html", {'empl':emp})
#    
#def employeedata(request):
#    if request.method == 'POST':
#        emp = EmployeeForm(request.POST)
#        if emp.is_valid():
#            emp.save()
#            return HttpResponseRedirect('/employee/empr/')
#    else:
#        emp = EmployeeForm()
#    return render(request, 'employee.html', {'employeedata':emp})
#
#def employeeread(request):
#    emp = Employee.objects.all()
#    return render(request, 'employeeread.html', {'employee':emp})
#
#def empd(request, id):
#    d = Employee.objects.get(pk=id)
#    d.delete()
#    return HttpResponseRedirect('/employee/empr')
#
#def empe(request, id):
#    z = Employee.objects.get(pk=id)
#    if request.method == 'POST':
#        e = EmployeeForm(request.POST, instance=z)
#        if e.is_valid():
#            e.save()
#            return HttpResponseRedirect('/employee/empr/')
#    else:
#        e = EmployeeForm(instance=z)
#        return render(request, 'employeeedit.html', {'employeeedit':e})
#
## View details of an employee
#class EmployeeDetail(DetailView):
#    model = Employee
#    template_name = 'employee_detail.html'
#    context_object_name = 'employee'
#
## Create a new employee
#class EmployeeCreate(View):
#    def get(self, request):
#        return render(request, 'employee_forms.html')
#
## Update an existing employee
#class EmployeeUpdate(UpdateView):
#    model = Employee
#    form_class = EmployeeForm
#    template_name = 'employe_forms.html'
#    success_url = reverse_lazy('employee_list')
#
## Delete an employee
#class EmployeeDelete(DeleteView):
#    model = Employee
#    template_name = 'employee_confirm_delete.html'
#    success_url = reverse_lazy('employee_list')
#
    #class based views

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Employee
from .forms import EmployeeForm
from django.core.paginator import Paginator
from .models import StaffPerformance, Qualification
from .forms import StaffPerformanceForm, QualificationForm
from .models import EmployeeDesignation

# List all employees
class EmployeeList(ListView):
    
    model = Employee
    template_name = 'employee_list.html'  # Specify the template name
    context_object_name = 'employees'     # Name to be used in the template for employees list
    paginate_by=10 # Number of records per page

     # Add search functionality
    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return Employee.objects.filter(employee_name__icontains=query)
        return Employee.objects.all()

# Create a new employee
class EmployeeCreate(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee_forms.html'  # Specify the template for creating a new employee
    success_url = reverse_lazy('employee_list')  # After a successful creation, redirect to employee list

# View details of an employee
class EmployeeDetail(DetailView):
    model = Employee
    template_name = 'employee_detail.html'  # Specify the template for employee details
    context_object_name = 'employee'  # Name to be used in the template for the employee

# Update an existing employee
class EmployeeUpdate(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee_forms.html'  # Reuse the form template for updating
    success_url = reverse_lazy('employee_list')  # Redirect to employee list after update

# Delete an employee
class EmployeeDelete(DeleteView):
    model = Employee
    template_name = 'employee_confirm_delete.html'  # Specify the template for confirming delete
    success_url = reverse_lazy('employee_list')  # Redirect to employee list after deletion

# StaffPerformance Views
class StaffPerformanceList(ListView):
    model = StaffPerformance
    template_name = 'staffperformance/staffperformance_list.html'

class StaffPerformanceDetail(DetailView):
    model = StaffPerformance
    template_name = 'staffperformance/staffperformance_detail.html'

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

class QualificationDetail(DetailView):
    model = Qualification
    template_name = 'qualification/qualification_detail.html'

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

#employee designation

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