
from django.db import models
from app.common.models import TimeStampedModel,Category,Religion,Nationality
from app.academic.models import Class,Section
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from core.utils.choices import GENDER_CHOICES, BLOOD_GROUP_CHOICES, PICK_N_DROP_CHOICES, CHILD_CHOICES, \
    HEALTH_CHOICES, IMMUNIZATION_CHOICES, GUARDIAN_RELATION_CHOICES, ENROLLMENT_CHOICES, \
    STUDENT_STATUS_CHOICES, ADMISSION_TYPE_CHOICES, VOUCHER_TYPE_CHOICES, SUBJECT_CHOICE


#! Stores personal information about the student

# Define choices for gender, blood group, health status, immunization, and disabilities

# Choices for Religion
# RELIGION_CHOICES = [
#     ('Islam', 'Islam'),
#     ('Christianity', 'Christianity'),
#     ('Hinduism', 'Hinduism'),
#     # Add more as needed
# ]

# # Choices for nationality (example)
# NATIONALITY_CHOICES = [
#     ('Pakistani', 'Pakistani'),
#     ('Indian', 'Indian'),
#     ('Bangladeshi', 'Bangladeshi'),
#     # Add more as needed
# ]

class PersonalInfo(TimeStampedModel):
    full_name = models.CharField(max_length=150, verbose_name="Full Name", help_text="Enter the full name of the individual.")
    date_of_birth = models.DateField(verbose_name="Date of Birth", help_text="Enter the date of birth.")
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, verbose_name="Gender", help_text="Select the gender.")
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES, verbose_name="Blood Group", help_text="Select the blood group.")
    place_of_birth = models.CharField(max_length=128, verbose_name="Place of Birth", help_text="Enter the place of birth.")
    current_address = models.CharField(max_length=255, verbose_name="Current Address", help_text="Enter the current address.")
    permanent_address = models.CharField(max_length=255, verbose_name="Permanent Address", help_text="Enter the permanent address.")
    mobile_number = models.CharField(max_length=11, validators=[RegexValidator(r'^\d{11}$', 'Enter a valid 11-digit mobile number.')], verbose_name="Mobile Number", help_text="Enter an 11-digit mobile number.")
    email = models.EmailField(verbose_name="Email Address", help_text="Enter a valid email address.")
    general_health = models.CharField(max_length=50, choices=HEALTH_CHOICES, verbose_name="General Health Status", help_text="Select general health status.")
    immunization = models.CharField(max_length=50, choices=IMMUNIZATION_CHOICES, verbose_name="Immunization Status", help_text="Select immunization status.")
    disabilities = models.CharField(max_length=255, blank=True, null=True, verbose_name="Disabilities", help_text="Enter any known disabilities, if any.")
    mark_of_identification = models.CharField(max_length=255, blank=True, null=True, verbose_name="Mark of Identification", help_text="Enter any identifying marks, if any.")

    class Meta:
        indexes = [
            models.Index(fields=['full_name'], name='full_name_idx'),
            models.Index(fields=['date_of_birth'], name='dob_idx'),
        ]

    def __str__(self):
        return self.full_name

# Stores parent/guardian information
class Occupation(models.Model):
    name = models.CharField(max_length=100, verbose_name="Occupation", help_text="Enter the occupation (e.g., Doctor, Engineer).")

    def __str__(self):
        return self.name
    

def validate_cnic(value):
    # Remove any hyphens
    if value:
        cleaned = value.replace('-', '')

        # Check if it's all digits and has a length of 13
        if not cleaned.isdigit() or len(cleaned) != 13:
            raise ValidationError('CNIC must have 13 digits.')

    return cleaned

class ParentInfo(TimeStampedModel):
    father_full_name = models.CharField(max_length=100, verbose_name="Father Full Name", help_text="Enter the father's full name.")
    father_cnic = models.CharField(max_length=15, validators=[validate_cnic], verbose_name="Father's CNIC", help_text="Enter the father's CNIC.")
    father_occupation = models.ForeignKey(Occupation, related_name='parentinfo_father_occupation', on_delete=models.CASCADE, verbose_name="Father's Occupation", help_text="Select father's occupation.")
    mother_full_name = models.CharField(max_length=100, verbose_name="Mother Full Name", help_text="Enter the mother's full name.") 
    mother_cnic = models.CharField(max_length=15, validators=[validate_cnic], verbose_name="Mother's CNIC", help_text="Enter the mother's CNIC.")
    mother_occupation = models.ForeignKey(Occupation, related_name='parentinfo_mother_occupation', on_delete=models.CASCADE, verbose_name="Mother's Occupation", help_text="Select mother's occupation.")
    mother_mobile_number = models.CharField(max_length=11, validators=[RegexValidator(r'^\d{11}$', 'Enter a valid 11-digit mobile number.')], verbose_name="Mother's Mobile Number", help_text="Enter the mother's 11-digit mobile number.")
    mother_email = models.EmailField(verbose_name="Mother's Email Address", help_text="Enter a valid email address.")
    mother_office_address = models.CharField(max_length=255, verbose_name="Mother's Office Address", help_text="Enter the mother's office address.")
    guardian_full_name = models.CharField(max_length=100, verbose_name="Guardian Full Name", help_text="Enter the guardian's full name.")
    guardian_cnic = models.CharField(max_length=15, validators=[validate_cnic], verbose_name="Guardian's CNIC", help_text="Enter the guardian's CNIC.")
    guardian_occupation = models.ForeignKey(Occupation, related_name='parentinfo_guardian_occupation', on_delete=models.CASCADE, verbose_name="Guardian's Occupation", help_text="Select guardian's occupation.")
    guardian_mobile_number = models.CharField(max_length=11, validators=[RegexValidator(r'^\d{11}$', 'Enter a valid 11-digit mobile number.')], verbose_name="Guardian's Mobile Number", help_text="Enter the guardian's 11-digit mobile number.")
    guardian_email = models.EmailField(verbose_name="Guardian's Email Address", help_text="Enter a valid email address.")
    guardian_home_address = models.CharField(max_length=255, verbose_name="Guardian's Home Address", help_text="Enter the guardian's home address.")
    guardian_office_address = models.CharField(max_length=255, verbose_name="Guardian's Office Address", help_text="Enter the guardian's office address.")
    guardian_relation_to_child = models.CharField(max_length=50, verbose_name="Guardian's Relation to Child", help_text="Enter the guardian's relation to the child.")

    class Meta:
        indexes = [
            models.Index(fields=['father_full_name'], name='father_name_idx'),
            models.Index(fields=['mother_full_name'], name='mother_name_idx'),
            models.Index(fields=['guardian_full_name'], name='guardian_name_idx'),
        ]

    def __str__(self):
        return self.father_full_name


#! Stores admission-related academic details like the class and section the student is admitted into.
class AcademicInfo(TimeStampedModel):
    admission_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='admitted_class', verbose_name="Admission Class")
    admission_section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name="Admission Section")
    admission_no = models.CharField(max_length=12, unique=True, blank=True, null=True, verbose_name="Admission Number", help_text="Unique admission number for the student")
    admission_type = models.CharField(max_length=50, choices=ADMISSION_TYPE_CHOICES, verbose_name="Admission Type", help_text="Type of admission (New/Transfer)")
    admission_confirmation_date = models.DateField(null=True, blank=True, verbose_name="Admission Confirmation Date", help_text="Date when admission was confirmed")
    marks_in_previous_school = models.PositiveIntegerField(null=True, blank=True, verbose_name="Marks in Previous School", help_text="Marks obtained in previous school")
    previous_school_roll_no = models.CharField(max_length=20, blank=True, null=True, verbose_name="Previous School Roll No", help_text="Roll number in the previous school")
    enrollment_status = models.CharField(max_length=50, choices=ENROLLMENT_CHOICES, verbose_name="Enrollment Status", help_text="Current enrollment status of the student")
    test_passed = models.BooleanField(default=False, verbose_name="Test Passed", help_text="Indicates whether the admission test was passed")

    class Meta:
        indexes = [
            models.Index(fields=['admission_no'], name='admission_no_idx'),
            models.Index(fields=['admission_confirmation_date'], name='adm_conf_date_idx'),  # Shortened index name
        ]

    def save(self, *args, **kwargs):
        if not self.admission_no:
            self.admission_no = self.generate_admission_no()
        super().save(*args, **kwargs)

    def generate_admission_no(self):
        last_admission = AcademicInfo.objects.last()
        if last_admission:
            return f"ADM{int(last_admission.admission_no[3:]) + 1:04d}"
        return "ADM0001"

    def __str__(self):
        return self.admission_type

class FinancialInfo(TimeStampedModel):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Category")
    fee_remaining_for_months = models.PositiveIntegerField(null=True, blank=True, verbose_name="Fee Remaining for Months (if any)", help_text="Number of months with remaining fees")
    monthly_income = models.PositiveIntegerField(null=True, blank=True, verbose_name="Monthly Income", help_text="Monthly income of the guardian")
    paid_dues_upto_slc = models.DateField(null=True, blank=True, verbose_name="Paid Dues up to School Leaving Certificate", help_text="Date of paid dues up to the SLC")

    class Meta:
        indexes = [
            models.Index(fields=['paid_dues_upto_slc'], name='paid_dues_upto_slc_idx'),
        ]

    def __str__(self):
        return str(self.category)


class AdditionalInfo(TimeStampedModel):
    nationality = models.ForeignKey(Nationality, on_delete=models.SET_NULL, null=True)
    religion = models.ForeignKey(Religion, on_delete=models.SET_NULL, null=True)
    extra_act = models.TextField(blank=True, null=True, verbose_name="Extracurricular Activities", help_text="Details of extracurricular activities")
    sibling = models.TextField(blank=True, null=True, verbose_name="Sibling Information", help_text="Information about siblings")
    remarks = models.TextField(blank=True, null=True, verbose_name="Remarks", help_text="Any additional remarks")
    is_alive = models.BooleanField(default=True, verbose_name="Is Alive", help_text="Indicates if the student is alive")
    is_security_voucher_generated = models.BooleanField(default=False, verbose_name="Security Voucher Generated", help_text="Indicates if a security voucher has been generated")
    is_voucher_generated = models.BooleanField(default=False, verbose_name="Voucher Generated", help_text="Indicates if a voucher has been generated")

    class Meta:
        indexes = [
            models.Index(fields=['nationality'], name='nationality_idx'),
        ]

    def __str__(self):
        return f"{self.religion} - {self.nationality}"


class Admission(TimeStampedModel):
    personal_info = models.OneToOneField(PersonalInfo, on_delete=models.CASCADE, verbose_name="Personal Information")
    parent_info = models.OneToOneField(ParentInfo, on_delete=models.CASCADE, verbose_name="Parent Information")
    academic_info = models.OneToOneField(AcademicInfo, on_delete=models.CASCADE, verbose_name="Academic Information")
    financial_info = models.OneToOneField(FinancialInfo, on_delete=models.CASCADE, verbose_name="Financial Information")
    additional_info = models.OneToOneField(AdditionalInfo, on_delete=models.CASCADE, verbose_name="Additional Information")

    def __str__(self):
        return self.personal_info.full_name


