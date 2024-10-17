'''
from django.db import models
# from app.admission.models import Admission
from app.common.models import TimeStampedModel


#!The main model that links to the admission data and tracks additional student-specific fields like roll number, status, and verification details.
class Student(TimeStampedModel,models.Model):
    admission = models.OneToOneField('Admission', on_delete=models.CASCADE,null=True)  
    roll_no = models.CharField(max_length=50)  
    is_verified = models.BooleanField(default=False)
    note = models.TextField(blank=True, null=True)  

    def __str__(self):
        return self.admission.personal_info.full_name  

'''