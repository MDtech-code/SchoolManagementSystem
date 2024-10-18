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
'''
from django.db import models
from app.common.models import TimeStampedModel
from django.contrib.auth.models import User



class Qualification(models.Model):
    # The BigAutoField is automatically the primary key, no need to explicitly define `id`

    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="qualifications")
    discipline = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    year_obtained = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.employee.username} ({self.year_obtained})"
    
class Leaves(models.Model):
    # The BigAutoField is automatically the primary key, no need to explicitly define `id`

    deducted_in_payroll = models.ForeignKey('Payroll', on_delete=models.SET_NULL, null=True, related_name="leaves_deducted")
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="employee_leaves")
    leave_type = models.ForeignKey('LeaveType', on_delete=models.CASCADE, related_name="leave_type_leaves")
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
    

class LeaveType(models.Model):
    # The BigAutoField is automatically the primary key, no need to explicitly define `id`

    name = models.CharField(max_length=100)
    days_paid = models.PositiveIntegerField()
    department = models.CharField(max_length=100)
    granted_times_in_service = models.PositiveIntegerField()
    granted_times_interval = models.PositiveIntegerField()

    def __str__(self):
        return self.name
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




'''