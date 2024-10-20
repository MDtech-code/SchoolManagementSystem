from django.db import models
from app.common.models import TimeStampedModel
from app.employee.models import Employee
from django.contrib.auth.models import User




class PayStructure(TimeStampedModel):
    employee_designation = models.ForeignKey('employee.EmployeeDesignation', on_delete=models.CASCADE)
    annual_increment = models.IntegerField()
    basic_pay = models.IntegerField()
    conveyance_allowance = models.IntegerField()
    hra = models.IntegerField()  # House Rent Allowance
    medical_allowance = models.IntegerField()

    def _str_(self):
        return f"{self.employee_designation.name} - Pay Structure"
    
class EmployeePayStructure(TimeStampedModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    employee_pay_structure = models.ForeignKey(PayStructure, on_delete=models.CASCADE)
    inc_aug_15_allowance = models.PositiveIntegerField()
    inc_aug_17_svc_allowance = models.PositiveIntegerField()
    inc_sep_21_svc_allowance = models.PositiveIntegerField()
    mphil_phd_allowance = models.PositiveIntegerField()
    spec_head_hunting_allowance = models.PositiveIntegerField()
    svc_allowance = models.PositiveIntegerField()

    def _str_(self):
        return f"{self.employee.employee_name} - Pay Structure"


class Payroll(TimeStampedModel):
    # The BigAutoField is automatically the primary key, no need to explicitly define `id`

    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payrolls")
    employee_pay_structure = models.ForeignKey(EmployeePayStructure, on_delete=models.CASCADE, related_name="payrolls")
    
    annual_increments = models.FloatField()
    arrears = models.PositiveIntegerField()
    conveyance_allowance = models.PositiveIntegerField()
    cp_fund = models.PositiveIntegerField()
    date_issued = models.DateField()
    education_allowance = models.PositiveIntegerField()
    employee_oldage_benefit_inst = models.PositiveIntegerField()
    eobi = models.PositiveIntegerField()
    house_rent_allowance = models.PositiveIntegerField()
    inc_aug_15_allowance = models.PositiveIntegerField()
    inc_aug_17_svc_allowance = models.PositiveIntegerField()
    inc_sep_21_svc_allowance = models.PositiveIntegerField()
    income_tax = models.PositiveIntegerField()
    increments = models.FloatField()
    is_paid = models.BooleanField(default=False)
    loan_installment = models.FloatField()
    lowp = models.PositiveIntegerField()
    medical_allowance = models.PositiveIntegerField()
    mphil_phd_allowance = models.PositiveIntegerField()
    pay_roll_no = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=50)
    security_deposit = models.PositiveIntegerField()
    spec_head_huntimg_allowance = models.PositiveIntegerField()
    svc_allowance = models.PositiveIntegerField()
    time_generated = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Payroll for {self.employee.username} - {self.total_amount}"
    

class EmployeeAnnualIncrement(TimeStampedModel):
    employee_structure = models.ForeignKey('EmployeePayStructure', on_delete=models.CASCADE, related_name="annual_increments")
    annual_inc_no = models.PositiveIntegerField()
    date_awarded = models.DateField()
    rate_of_annual_inc = models.CharField(max_length=100)
    total_annual_inc = models.PositiveIntegerField()

    def __str__(self):
        return f"Annual Increment #{self.annual_inc_no} for {self.employee_structure} - {self.total_annual_inc}"
    
class IncrementOrder(TimeStampedModel):
    created = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=255)
    percentage_increment = models.FloatField()

    def __str__(self):
        return f"Increment Order - {self.percentage_increment}%"
class Increment(TimeStampedModel):
    order = models.ForeignKey(IncrementOrder, on_delete=models.CASCADE, related_name="increments")
    pay_structure = models.ForeignKey(EmployeePayStructure, on_delete=models.CASCADE, related_name="increments")
    amount = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Increment for {self.pay_structure} - {self.amount}"
class LeaveType(TimeStampedModel):
    # The BigAutoField is automatically the primary key, no need to explicitly define `id`

    name = models.CharField(max_length=100)
    days_paid = models.PositiveIntegerField()
    department = models.CharField(max_length=100)
    granted_times_in_service = models.PositiveIntegerField()
    granted_times_interval = models.PositiveIntegerField()

    def __str__(self):
        return self.name
class Leaves(TimeStampedModel):
    # The BigAutoField is automatically the primary key, no need to explicitly define `id`

    deducted_in_payroll = models.ForeignKey(Payroll, on_delete=models.SET_NULL, null=True, related_name="leaves_deducted")
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="employee_leaves")
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE, related_name="leave_type_leaves")
    deductions = models.PositiveIntegerField()
    executive_approval = models.BooleanField(default=False)
    leave_date = models.DateField()
    leave_end_date = models.DateField()
    note = models.TextField(blank=True)
    principal_approval = models.BooleanField(default=False)
    reason = models.TextField()
    request_date = models.DateField(auto_now_add=True)
    secretary_approval = models.BooleanField(default=False)
    status = models.CharField(max_length=50)
    vc_approval = models.BooleanField(default=False)

    def __str__(self):
        return f"Leave for {self.employee.username} - {self.status}"
    



