
from django.db import models
from app.admission.models import Admission
from app.common.models import TimeStampedModel

#!The main model that links to the admission data and tracks additional student-specific fields like roll number, status, and verification details.
class Student(TimeStampedModel):
    """
    The main model that links to the admission data and tracks additional
    student-specific fields like roll number, status, and verification details.
    """

    #! A one-to-one relationship with the Admission model
    admission = models.OneToOneField(
        Admission,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Admission Record",
        help_text="The admission record associated with this student."
    )  
    
    #! Roll number for the student, must be unique
    roll_no = models.CharField(
        max_length=50,
        unique=True,  #! Ensures that each roll number is unique
        verbose_name="Roll Number",
        help_text="Unique roll number assigned to the student."
    )  
    
    #! Boolean field to check if the student is verified
    is_verified = models.BooleanField(
        default=False,
        verbose_name="Verification Status",
        help_text="Indicates whether the student has been verified."
    )
    
    #! Notes related to the student, optional
    note = models.TextField(
        blank=True,
        null=True,
        verbose_name="Additional Notes",
        help_text="Any additional notes regarding the student."
    )  

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['roll_no'], name='unique_roll_no')  #! Unique constraint on roll number
        ]
        indexes = [
            models.Index(fields=['roll_no'], name='roll_no_idx')  #! Index for faster lookups on roll number
        ]
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return self.admission.personal_info.full_name
