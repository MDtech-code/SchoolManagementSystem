'''
from django.db import models
from app.common.models import TimeStampedModel
from app.employee.models import Employee
from django.contrib.auth.models import User


class Bank(TimeStampedModel,models.Model):
    id = models.BigAutoField(primary_key=True)
    bank_account_no = models.CharField(max_length=255)
    bank_address = models.CharField(max_length=255)
    bank_code = models.CharField(max_length=255)
    bank_contact = models.IntegerField()
    bank_for_security = models.BooleanField()
    bank_manager = models.CharField(max_length=255)
    bank_name = models.CharField(max_length=255)
    show_on_voucher = models.BooleanField()

    def __str__(self):
        return self.bank_name


class Expense(TimeStampedModel,models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField()
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
'''
'''


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


class CPFund(models.Model):
    # The BigAutoField is automatically the primary key in Django, so no need to explicitly define `id`
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_funds")
    employee = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cpfund")
    deposited_cp_fund = models.PositiveIntegerField()
    last_date_submitted = models.DateField()

    def __str__(self):
        return f"CPFund for {self.employee.username} - {self.deposited_cp_fund}"


class EOBIPaid(models.Model):
    # The BigAutoField is automatically the primary key, no need to explicitly define `id`
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="eobi_created_by")
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="eobi_employee")
    eobi_date_of_joining = models.DateField()
    month = models.DateField()
    total_deposit = models.FloatField()

    def __str__(self):
        return f"EOBI Payment for {self.employee.username} - {self.total_deposit}"
    
class CPFundDeposits(models.Model):
    # The BigAutoField is automatically the primary key, no need to explicitly define `id`
    
    cp_fund = models.ForeignKey(CPFund, on_delete=models.CASCADE, related_name="deposits")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cpfund_deposits_created_by")
    amount = models.PositiveIntegerField()
    date_paid = models.DateField()
    note = models.CharField(max_length=255)

    def __str__(self):
        return f"CPFund Deposit of {self.amount} by {self.created_by.username} on {self.date_paid}"
    

class EmployeeArrears(models.Model):
    # The BigAutoField is automatically the primary key, no need to explicitly define `id`
    
    employee = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employee_arrears")
    arrears_amount = models.IntegerField()
    arrears_note = models.CharField(max_length=255)

    def __str__(self):
        return f"Arrears for {self.employee.username} - {self.arrears_amount}"

'''