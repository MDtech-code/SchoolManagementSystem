from django.db import models
from app.common.models import TimeStampedModel
from django.contrib.auth.models import User

class EmployeeDesignation(TimeStampedModel):
    department = models.CharField(max_length=255)
    description = models.TextField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Employee(TimeStampedModel):
    designation = models.ForeignKey(EmployeeDesignation, on_delete=models.CASCADE)
    employee_pay_structure = models.ForeignKey('payroll.PayStructure', on_delete=models.CASCADE)
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


class StaffPerformance(TimeStampedModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    comments = models.TextField()
    rating = models.PositiveSmallIntegerField()
    date_evaluated = models.DateField()

    def __str__(self):
        return f"Performance Evaluation for {self.employee.employee_name} on {self.date_evaluated}"

class Qualification(TimeStampedModel):
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="qualifications")
    discipline = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    year_obtained = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.employee.username} ({self.year_obtained})"
    

