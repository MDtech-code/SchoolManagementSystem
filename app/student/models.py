from django.db import models
from django.conf import settings
from app.common.models import TimeStampedModel
from core.utils.choices import STUDENT_STATUS_CHOICES



class Student(TimeStampedModel):
    """
    Stores comprehensive information about a student, linked to their 
    admission record. Includes an auto-generated, semantic roll number, 
    verification status, academic history, and contact details.
    """

    admission = models.OneToOneField(
        'admission.Admission',
        on_delete=models.CASCADE,
        null=True,  # Allow null initially, but validate later
        verbose_name="Admission Record",
        help_text="The related admission record."
    )
    user = models.ForeignKey( 
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='students', 
        verbose_name="Linked User Account",
        help_text="The user account associated with this student (parent/guardian)."
    )
    roll_no = models.CharField(
        max_length=50,
        unique=True,
        editable=False,
        null=True,  # Prevent manual editing
        verbose_name="Roll Number",
        help_text="Auto-generated semantic roll number."
    )
    is_verified = models.BooleanField(
        default=False,
        verbose_name="Verification Status",
        null=True,
        help_text="Indicates whether the student has been verified."
    )
    student_status = models.CharField(
        max_length=20,
        choices=STUDENT_STATUS_CHOICES,
        default='enrolled',
        verbose_name="Student Status",
        null=True,
        help_text="Current status of the student."
    )
    # ... (Add fields for current class, section, contact info, etc.)
    note = models.TextField(
        blank=True,
        null=True,
        verbose_name="Additional Notes",
        help_text="Any additional notes regarding the student."
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['roll_no'], name='unique_roll_no')
        ]
        indexes = [
            models.Index(fields=['roll_no'], name='roll_no_idx')
        ]
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return self.admission.full_name 

    def save(self, *args, **kwargs):
        if not self.roll_no:  # Generate roll number only if it's not set
            self.roll_no = self.generate_roll_no()
        super().save(*args, **kwargs)

    def generate_roll_no(self):
        """Generates a semantic roll number based on class and sequence."""
        last_student = Student.objects.filter(
            admission__admission_class=self.admission.admission_class  # Accessing related fields
        ).order_by('-roll_no').first()

        if last_student:
            last_roll_no = last_student.roll_no
            try:
                prefix, sequence = last_roll_no.split('-')  # Assuming format "CLASS-SEQ"
                sequence = int(sequence) + 1
            except ValueError:
                sequence = 1  # Start with 1 if no previous roll number
        else:
            prefix = self.admission.admission_class.name[:3].upper()  # Get class name prefix
            sequence = 1

        return f"{prefix}-{sequence:03d}"  # Format with leading zeros












