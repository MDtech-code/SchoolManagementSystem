
from django.db import models
from app.common.models import TimeStampedModel


class Class(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)
    label = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
class Department(TimeStampedModel):
    name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name


class Section(TimeStampedModel):
    name = models.CharField(max_length=50, blank=True, null=True)
    section_of_class = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.section_of_class}-{self.name}"


class Subjects(TimeStampedModel):
    subject_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject_type = models.CharField(max_length=64)
    name = models.CharField(max_length=264)

    def __str__(self):
        return self.name
    
class SchoolLeavingCertificate(TimeStampedModel):
    admission_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='slc_admission_class')
    last_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='slc_last_class')
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE)
    admission_date = models.DateField()
    arrears_remaining = models.PositiveIntegerField()
    is_refunded = models.BooleanField()
    leaving_date = models.DateField(null=True, blank=True)
    paid_to = models.CharField(max_length=255)
    received_by = models.CharField(max_length=255)
    refund_date = models.DateField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    security_refunded = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.student} - {self.admission_class}"
