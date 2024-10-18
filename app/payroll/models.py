'''
from django.db import models
from app.employee.models import Employee
from django.contrib.auth.models import User


class Payroll(models.Model):
    # The BigAutoField is automatically the primary key, no need to explicitly define `id`

    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payrolls")
    employee_pay_structure = models.ForeignKey('EmployeePayStructure', on_delete=models.CASCADE, related_name="payrolls")
    
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
    

class EmployeeAnnualIncrement(models.Model):
    # The BigAutoField is automatically the primary key, no need to explicitly define `id`
    
    employee_structure = models.ForeignKey('EmployeePayStructure', on_delete=models.CASCADE, related_name="annual_increments")
    annual_inc_no = models.PositiveIntegerField()
    date_awarded = models.DateField()
    rate_of_annual_inc = models.CharField(max_length=100)
    total_annual_inc = models.PositiveIntegerField()

    def __str__(self):
        return f"Annual Increment #{self.annual_inc_no} for {self.employee_structure} - {self.total_annual_inc}"
    

class Increment(models.Model):
    # The BigAutoField is automatically the primary key, no need to explicitly define `id`

    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name="increments")
    pay_structure = models.ForeignKey('EmployeePayStructure', on_delete=models.CASCADE, related_name="increments")
    amount = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Increment for {self.pay_structure} - {self.amount}"


class IncrementOrder(models.Model):
    # The BigAutoField is automatically the primary key, no need to explicitly define `id`
    
    created = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=255)
    percentage_increment = models.FloatField()

    def __str__(self):
        return f"Increment Order - {self.percentage_increment}%"

'''