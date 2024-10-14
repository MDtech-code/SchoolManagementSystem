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