

# Register your models here.
from django.contrib import admin
from .models import (
    EmployeeDesignation,
    PayStructure,
    Employee,
    EmployeePayStructure,
    EmployeeAnnualIncrement,
    Qualification,
)

@admin.register(EmployeeDesignation)
class EmployeeDesignationAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'description')

@admin.register(PayStructure)
class PayStructureAdmin(admin.ModelAdmin):
    list_display = ('employee_designation', 'basic_pay', 'annual_increment')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_name', 'designation', 'date_of_joining', 'employee_status')

@admin.register(EmployeePayStructure)
class EmployeePayStructureAdmin(admin.ModelAdmin):
    list_display = ('employee', 'employee_pay_structure', 'svc_allowance')

@admin.register(EmployeeAnnualIncrement)
class EmployeeAnnualIncrementAdmin(admin.ModelAdmin):
    list_display = ('employee_structure', 'annual_inc_no', 'date_awarded')

@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    list_display = ('employee', 'discipline', 'institution', 'year_obtained')

