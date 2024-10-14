'''
from django.db import models
from student.models import Student, Class, Section

class Admission(models.Model):
    admission_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, related_name='admitted_class')
    admission_section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)
    full_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    father_cnic = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='admissions')

    def __str__(self):
        return f"Admission: {self.full_name} ({self.father_name})"
'''