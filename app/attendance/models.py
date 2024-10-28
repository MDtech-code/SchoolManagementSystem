
from django.db import models
from app.student.models import Student
from app.common.models import TimeStampedModel

class Attendance(TimeStampedModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField()

    def __str__(self):
        return f"{self.student} - {self.date} - {'Present' if self.is_present else 'Absent'}"


class StaffAttendance(models.Model):
    employee = models.ForeignKey('employee.Employee', on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField(default=False)
    is_late = models.BooleanField(default=False)
    is_excused = models.BooleanField(default=False)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.employee} - {self.date} - Present: {self.is_present}'
