'''
from django.db import models

class Employee(models.Model):
    employee_name = models.CharField(max_length=255)
    employee_id = models.CharField(max_length=50, unique=True)
    designation = models.ForeignKey('EmployeeDesignation', on_delete=models.SET_NULL, null=True)
    date_of_joining = models.DateField()
    contact_number = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.employee_name} ({self.employee_id})"

class EmployeeDesignation(models.Model):
    department = models.CharField(max_length=255)
    description = models.TextField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Qualification(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    discipline = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    year_obtained = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.employee.employee_name} - {self.discipline}"

'''
from django.db import models
from app.common.models import TimeStampedModel
class EmployeeDesignation(TimeStampedModel,models.Model):
    department = models.CharField(max_length=255)
    description = models.TextField()
    name = models.CharField(max_length=255)

    def _str_(self):
        return self.name


class PayStructure(models.Model):
    employee_designation = models.ForeignKey(EmployeeDesignation, on_delete=models.CASCADE)
    annual_increment = models.IntegerField()
    basic_pay = models.IntegerField()
    conveyance_allowance = models.IntegerField()
    hra = models.IntegerField()  # House Rent Allowance
    medical_allowance = models.IntegerField()

    def _str_(self):
        return f"{self.employee_designation.name} - Pay Structure"


class Employee(models.Model):
    designation = models.ForeignKey(EmployeeDesignation, on_delete=models.CASCADE)
    employee_pay_structure = models.ForeignKey(PayStructure, on_delete=models.CASCADE)
    account_no = models.CharField(max_length=100)
    address = models.TextField()
    bank = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    cnic = models.CharField(max_length=20)
    contact_no = models.CharField(max_length=15)
    country = models.CharField(max_length=100)
    covid_vaccinated = models.BooleanField(default=False)
    date_of_birth = models.DateField()
    date_of_joining = models.DateField()
    date_of_rejoining = models.DateField(null=True, blank=True)
    date_of_resignation = models.DateField(null=True, blank=True)
    email = models.EmailField()
    employee_id = models.CharField(max_length=50)
    employee_name = models.CharField(max_length=255)
    employee_status = models.CharField(max_length=50)
    father_cnic = models.CharField(max_length=20)
    father_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    is_verified = models.BooleanField(default=False)
    martial_status = models.CharField(max_length=50)
    note = models.TextField(null=True, blank=True)
    province = models.CharField(max_length=100)
    wing = models.CharField(max_length=100)

    def _str_(self):
        return self.employee_name


class EmployeePayStructure(models.Model):
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


class EmployeeAnnualIncrement(models.Model):
    employee_structure = models.ForeignKey(EmployeePayStructure, on_delete=models.CASCADE)
    annual_inc_no = models.PositiveIntegerField()
    date_awarded = models.DateField()
    rate_of_annual_inc = models.CharField(max_length=50)
    total_annual_inc = models.PositiveIntegerField()

    def _str_(self):
        return f"Annual Increment {self.annual_inc_no} for {self.employee_structure.employee.employee_name}"


class Qualification(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    discipline = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    year_obtained = models.PositiveIntegerField()

    def _str_(self):
        return f"{self.employee.employee_name} - {self.name}"