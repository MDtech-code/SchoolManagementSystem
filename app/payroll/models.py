'''
from django.db import models
from employee.models import Employee

class PayStructure(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    basic_pay = models.PositiveIntegerField(default=0)
    allowances = models.PositiveIntegerField(default=0)
    deductions = models.PositiveIntegerField(default=0)
    total_pay = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Pay Structure for {self.employee.employee_name}"

class EmployeePayStructure(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    pay_structure = models.ForeignKey(PayStructure, on_delete=models.CASCADE)

    def __str__(self):
        return f"Employee Pay Structure - {self.employee.employee_name}"

class EmployeeAnnualIncrement(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    annual_increment = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Annual Increment for {self.employee.employee_name}"

class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    basic_pay = models.PositiveIntegerField(default=0)
    allowances = models.PositiveIntegerField(default=0)
    deductions = models.PositiveIntegerField(default=0)
    total_pay = models.PositiveIntegerField(default=0)
    pay_date = models.DateField()

    def __str__(self):
        return f"Payroll - {self.employee.employee_name} ({self.pay_date})"
'''