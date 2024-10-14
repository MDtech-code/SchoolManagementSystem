'''
from django.db import models
from employee.models import Employee

class Loan(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    loan_amount = models.FloatField()
    remaining_amount = models.FloatField()
    total_installments = models.PositiveIntegerField()

    def __str__(self):
        return f"Loan for {self.employee.employee_name}"

class InstallmentPaid(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    amount_paid = models.FloatField()
    date_paid = models.DateField()

    def __str__(self):
        return f"Installment Paid for {self.loan.employee.employee_name}"

class IncomeTaxSession(models.Model):
    starting_year = models.DateField()
    ending_year = models.DateField()

    def __str__(self):
        return f"Income Tax Session {self.starting_year} - {self.ending_year}"

class IncomeTaxRates(models.Model):
    session = models.ForeignKey(IncomeTaxSession, on_delete=models.CASCADE)
    initial_taxable_income = models.PositiveIntegerField()
    to_taxable_income = models.PositiveIntegerField()
    percentage = models.FloatField()

    def __str__(self):
        return f"Tax Rate for {self.session}"

class LeaveType(models.Model):
    name = models.CharField(max_length=50)
    days_paid = models.PositiveIntegerField()
    granted_times_in_service = models.PositiveIntegerField()
    granted_times_interval = models.PositiveIntegerField()

    def __str__(self):
        return self.name
'''