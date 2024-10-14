from django.db import models
from app.common.models import TimeStampedModel
# Create your models here.



'''

class Nationality(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Religion(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Province(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Class(models.Model):
    name = models.CharField(max_length=50)
    label = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=50)
    section_of_class = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.section_of_class.name} - {self.name}"

class Student(models.Model):
    student_name = models.CharField(max_length=256)
    roll_no = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=64)
    date_of_birth = models.DateField()
    father_name = models.CharField(max_length=256)
    father_cnic = models.CharField(max_length=15)
    address = models.CharField(max_length=256)
    religion = models.ForeignKey(Religion, on_delete=models.SET_NULL, null=True)
    nationality = models.ForeignKey(Nationality, on_delete=models.SET_NULL, null=True)
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True)
    student_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)
    student_section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)
    contact_number = models.CharField(max_length=256)
    date_of_admission = models.DateField()
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student_name} ({self.roll_no})"
'''