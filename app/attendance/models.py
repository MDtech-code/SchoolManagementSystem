

'''
from django.db import models
from employee.models import Employee

class StaffAttendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField()
    is_late = models.BooleanField()
    on_leave = models.BooleanField()

    def __str__(self):
        return f"Attendance for {self.employee.employee_name} on {self.date}"

class StaffPerformance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    comments = models.TextField()
    rating = models.PositiveSmallIntegerField()
    date_evaluated = models.DateField()

    def __str__(self):
        return f"Performance Evaluation for {self.employee.employee_name} on {self.date_evaluated}"

'''