
# from django.contrib import admin
# from .models import PayStructure, EmployeePayStructure, Payroll, EmployeeAnnualIncrement, IncrementOrder, Increment, LeaveType, Leaves

# @admin.register(PayStructure)
# class PayStructureAdmin(admin.ModelAdmin):
#     list_display = ('employee_designation', 'annual_increment', 'basic_pay', 'conveyance_allowance', 'hra', 'medical_allowance')
#     search_fields = ('employee_designation__name',)
#     list_filter = ('employee_designation',)
#     ordering = ('employee_designation',)

# @admin.register(EmployeePayStructure)
# class EmployeePayStructureAdmin(admin.ModelAdmin):
#     list_display = ('employee', 'employee_pay_structure', 'inc_aug_15_allowance', 'inc_aug_17_svc_allowance', 'inc_sep_21_svc_allowance', 'mphil_phd_allowance', 'spec_head_hunting_allowance', 'svc_allowance')
#     search_fields = ('employee__employee_name',)
#     list_filter = ('employee',)
#     ordering = ('employee',)

# @admin.register(Payroll)
# class PayrollAdmin(admin.ModelAdmin):
#     list_display = ('employee', 'employee_pay_structure', 'date_issued', 'total_amount', 'is_paid')
#     search_fields = ('employee__username', 'pay_roll_no')
#     list_filter = ('date_issued', 'is_paid')
#     date_hierarchy = 'date_issued'
#     ordering = ('-date_issued',)

# @admin.register(EmployeeAnnualIncrement)
# class EmployeeAnnualIncrementAdmin(admin.ModelAdmin):
#     list_display = ('employee_structure', 'annual_inc_no', 'date_awarded', 'total_annual_inc')
#     search_fields = ('employee_structure__employee__employee_name',)
#     list_filter = ('date_awarded',)
#     date_hierarchy = 'date_awarded'
#     ordering = ('-date_awarded',)

# @admin.register(IncrementOrder)
# class IncrementOrderAdmin(admin.ModelAdmin):
#     list_display = ('created', 'note', 'percentage_increment')
#     search_fields = ('note',)
#     ordering = ('-created',)

# @admin.register(Increment)
# class IncrementAdmin(admin.ModelAdmin):
#     list_display = ('order', 'pay_structure', 'amount', 'created')
#     search_fields = ('order__note', 'pay_structure__employee__employee_name')
#     list_filter = ('created',)
#     date_hierarchy = 'created'
#     ordering = ('-created',)

# @admin.register(LeaveType)
# class LeaveTypeAdmin(admin.ModelAdmin):
#     list_display = ('name', 'days_paid', 'department', 'granted_times_in_service', 'granted_times_interval')
#     search_fields = ('name', 'department')
#     list_filter = ('department',)
#     ordering = ('name',)

# @admin.register(Leaves)
# class LeavesAdmin(admin.ModelAdmin):
#     list_display = ('employee', 'leave_type', 'leave_date', 'leave_end_date', 'status', 'executive_approval', 'principal_approval', 'secretary_approval', 'vc_approval')
#     search_fields = ('employee__username', 'leave_type__name')
#     list_filter = ('leave_date', 'status', 'executive_approval', 'principal_approval', 'secretary_approval', 'vc_approval')
#     date_hierarchy = 'leave_date'
#     ordering = ('-leave_date',)
