from django.db import models
from app.common.models import TimeStampedModel
from django.contrib.auth.models import User
from django.utils import timezone
from app.account.models import CustomUser


class EmployeeDesignation(TimeStampedModel):
    department = models.CharField(max_length=255, verbose_name='Department', help_text='Enter the name of the department.')
    description = models.TextField(verbose_name='Description', help_text='Provide a brief description of the designation.')
    name = models.CharField(max_length=255, verbose_name='Designation Name', help_text='Enter the name of the designation.', unique=True)

    def __str__(self):
        return self.name


class Employee(TimeStampedModel):
    designation = models.ForeignKey(EmployeeDesignation, on_delete=models.CASCADE, verbose_name='Designation')
    employee_pay_structure = models.ForeignKey('payroll.PayStructure', on_delete=models.CASCADE, verbose_name='Pay Structure')
    account_no = models.CharField(max_length=20, verbose_name='Account Number', help_text='Enter the employee\'s bank account number.')
    address = models.TextField(verbose_name='Address', help_text='Enter the employee\'s residential address.')
    bank = models.CharField(max_length=100, verbose_name='Bank Name', help_text='Enter the name of the bank.')
    city = models.CharField(max_length=50, verbose_name='City', help_text='Enter the city where the employee resides.')
    cnic = models.CharField(max_length=15, verbose_name='CNIC', help_text='Enter the employee\'s CNIC number.', unique=True)
    contact_no = models.CharField(max_length=11, verbose_name='Contact Number', help_text='Enter the employee\'s contact number.', unique=True)
    country = models.CharField(max_length=50, verbose_name='Country', help_text='Enter the employee\'s country of residence.')
    covid_vaccinated = models.BooleanField(default=False, verbose_name='COVID Vaccinated', help_text='Indicate whether the employee is vaccinated against COVID-19.')
    date_of_birth = models.DateField(verbose_name='Date of Birth', help_text='Enter the employee\'s date of birth.')
    date_of_joining = models.DateField(verbose_name='Date of Joining', help_text='Enter the date when the employee joined the organization.')
    date_of_rejoining = models.DateField(null=True, blank=True, verbose_name='Date of Rejoining', help_text='Enter the date of rejoining if applicable.')
    date_of_resignation = models.DateField(null=True, blank=True, verbose_name='Date of Resignation', help_text='Enter the date of resignation if applicable.')
    email = models.EmailField(verbose_name='Email', help_text='Enter the employee\'s email address.', unique=True)
    employee_id = models.CharField(max_length=20, verbose_name='Employee ID', help_text='Enter a unique employee ID.', unique=True)
    employee_name = models.CharField(max_length=100, verbose_name='Employee Name', help_text='Enter the full name of the employee.')
    employee_status = models.CharField(max_length=20, verbose_name='Employee Status', help_text='Enter the status of the employee (e.g., active, inactive).')
    father_cnic = models.CharField(max_length=15, verbose_name='Father\'s CNIC', help_text='Enter the CNIC of the employee\'s father.')
    father_name = models.CharField(max_length=100, verbose_name='Father\'s Name', help_text='Enter the name of the employee\'s father.')
    gender = models.CharField(max_length=6, verbose_name='Gender', help_text='Enter the employee\'s gender (e.g., male, female).')
    is_verified = models.BooleanField(default=False, verbose_name='Is Verified', help_text='Indicate whether the employee\'s details are verified.')
    martial_status = models.CharField(max_length=10, verbose_name='Marital Status', help_text='Enter the marital status of the employee.')
    note = models.TextField(null=True, blank=True, verbose_name='Notes', help_text='Additional notes about the employee.')
    province = models.CharField(max_length=50, verbose_name='Province', help_text='Enter the province or state of residence.')
    wing = models.CharField(max_length=50, verbose_name='Wing', help_text='Enter the wing of the employee in the organization.')

    class Meta:
        indexes = [
            models.Index(fields=['employee_id'], name='employee_id_idx'),
        ]

    def __str__(self):
        return self.employee_name


class StaffPerformance(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, verbose_name='Employee')
    comments = models.TextField(verbose_name='Comments', help_text='Enter performance evaluation comments.')
    rating = models.PositiveSmallIntegerField(verbose_name='Rating', help_text='Enter a rating from 1 to 5.')
    date_evaluated = models.DateField(verbose_name='Date Evaluated', help_text='Enter the date of evaluation.')

    def __str__(self):
        return f"Performance Evaluation for {self.employee.employee_name} on {self.date_evaluated}"


class Qualification(TimeStampedModel):
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="qualifications", verbose_name='Employee')
    discipline = models.CharField(max_length=100, verbose_name='Discipline', help_text='Enter the discipline of the qualification.')
    institution = models.CharField(max_length=100, verbose_name='Institution', help_text='Enter the name of the institution.')
    name = models.CharField(max_length=100, verbose_name='Qualification Name', help_text='Enter the name of the qualification.')
    year_obtained = models.PositiveIntegerField(verbose_name='Year Obtained', help_text='Enter the year when the qualification was obtained.')

    def __str__(self):
         return f"{self.name} - {self.employee.username} ({self.year_obtained})"
