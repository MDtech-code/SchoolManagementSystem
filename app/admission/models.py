
from django.db import models
from django.conf import settings
from app.common.models import TimeStampedModel
from core.utils.choices import (
    GENDER_CHOICES, 
    BLOOD_GROUP_CHOICES, 
    HEALTH_CHOICES, 
    IMMUNIZATION_CHOICES,GUARDIAN_RELATION_CHOICES,PICK_N_DROP_CHOICES,
    ADMISSION_TYPE_CHOICES,
    ENROLLMENT_CHOICES,ADMISSION_STATUS,
    VOUCHER_TYPE_CHOICES,
    SUBJECT_CHOICE
)
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import transaction  # For transaction management

# from app.academic.models import Class, Section
class Occupation(TimeStampedModel):
    """
    Stores a list of occupations, which can be associated with parents or
    guardians.
    """
    name = models.CharField(
        max_length=100,
        verbose_name="Occupations",
        help_text="Enter the occupation (e.g., Doctor, Engineer).",
    )

    def __str__(self):
        return self.name




def validate_cnic(value):
    """
    Validates a CNIC number to ensure it has 13 digits.
    """
    if value:
        cleaned = value.replace("-", "")
        if not cleaned.isdigit() or len(cleaned) != 13:
            raise ValidationError("CNIC must have 13 digits.")
    return cleaned



class Admission(TimeStampedModel):
    """
    Represents a student's admission record, consolidating information from 
    various related models: PersonalInfo, ParentInfo, AcademicInfo, 
    FinancialInfo, and AdditionalInfo.
    """
    applicant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Applicant"
    )

    # Personal Information
    full_name = models.CharField(max_length=150)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    # place_of_birth = models.CharField(max_length=128)
    current_address = models.CharField(max_length=255)
    permanent_address = models.CharField(max_length=255)
    mobile_number = models.CharField(
        max_length=11,
        validators=[
            RegexValidator(
                r"^\d{11}$", "Enter a valid 11-digit mobile number."
            )
        ]
    )
    email = models.EmailField()
    general_health = models.CharField(max_length=50, choices=HEALTH_CHOICES)
    immunization = models.CharField(max_length=50, choices=IMMUNIZATION_CHOICES)
    disabilities = models.CharField(max_length=255, blank=True, null=True)
    mark_of_identification = models.CharField(max_length=255, blank=True, null=True)
    # child = models.CharField(max_length=100, blank=True, null=True)
    # form_b_no = models.CharField(max_length=50, blank=True, null=True)
    phone_residence = models.CharField(max_length=15, blank=True, null=True)
    # office_address = models.CharField(max_length=255, blank=True, null=True)

    # Parent Information
    father_full_name = models.CharField(max_length=100)
    father_cnic = models.CharField(max_length=15)
    father_occupation = models.ForeignKey('Occupation',on_delete=models.SET_NULL,null=True,blank=True,related_name='father_occupations')  # Changed to CharField
    mother_full_name = models.CharField(max_length=100)
    mother_cnic = models.CharField(max_length=15)
    mother_occupation =models.ForeignKey('Occupation',on_delete=models.SET_NULL,null=True,blank=True,related_name='mother_occupations')
    mother_mobile_number = models.CharField(max_length=11)
    mother_email = models.EmailField()
    #mother_office_address = models.CharField(max_length=255)
    mother_is_alive = models.BooleanField(default=True)

    # Guardian Information
    guardian_full_name = models.CharField(max_length=100, blank=True, null=True)
    guardian_cnic = models.CharField(max_length=15, blank=True, null=True)
    guardian_occupation =models.ForeignKey('Occupation',on_delete=models.SET_NULL,null=True,blank=True,related_name='guardian_occupations') # Changed to CharField
    guardian_mobile_number = models.CharField(max_length=11, blank=True, null=True)
    guardian_email = models.EmailField(blank=True, null=True)
    guardian_home_address = models.CharField(max_length=255, blank=True, null=True)
    guardian_office_address = models.CharField(max_length=255, blank=True, null=True)
    guardian_relation_to_child = models.CharField(max_length=50, choices=GUARDIAN_RELATION_CHOICES)
    guardian_pick_and_drop = models.CharField(max_length=20, choices=PICK_N_DROP_CHOICES)
    guardian_pick_and_drop_by = models.CharField(max_length=100, blank=True, null=True)
    guardian_pick_and_drop_cnic = models.CharField(max_length=15, blank=True, null=True)

    # Academic Information
    admission_class = models.ForeignKey('academic.Class', on_delete=models.CASCADE)
    admission_section = models.ForeignKey('academic.Section', on_delete=models.CASCADE)
    admission_no = models.CharField(max_length=12, unique=True, blank=True, null=True)
    admission_type = models.CharField(max_length=50, choices=ADMISSION_TYPE_CHOICES)
    #marks_in_previous_school = models.PositiveIntegerField(null=True, blank=True)
    #previous_school_roll_no = models.CharField(max_length=20, blank=True, null=True)
    #enrollment_status = models.CharField(max_length=50, choices=ENROLLMENT_CHOICES)
    test_passed = models.BooleanField(default=False)
    class_required = models.ForeignKey(
        'academic.Class', 
        on_delete=models.CASCADE, 
        related_name='required_class' 
    )

    # Financial Information
    category = models.ForeignKey('common.Category', on_delete=models.PROTECT)
    #fee_remaining_for_months = models.PositiveIntegerField(null=True, blank=True)
    #monthly_income = models.PositiveIntegerField(null=True, blank=True)
    #paid_dues_upto_slc = models.DateField(null=True, blank=True)
    #advance = models.PositiveIntegerField(default=0)
    #arrears = models.PositiveIntegerField(default=0)
    #total_arrear_months = models.PositiveIntegerField(default=0)

    # Additional Information
    nationality = models.ForeignKey('common.Nationality', on_delete=models.SET_NULL, null=True)
    religion = models.ForeignKey('common.Religion', on_delete=models.SET_NULL, null=True)
    # extra_act = models.TextField(blank=True, null=True)
    sibling = models.TextField(blank=True, null=True)
    # remarks = models.TextField(blank=True, null=True)
    is_alive = models.BooleanField(default=True)
    is_security_voucher_generated = models.BooleanField(default=False)
    is_voucher_generated = models.BooleanField(default=False)
    admission_by = models.CharField(max_length=100)
    # other_information = models.TextField(blank=True, null=True)

    admission_status = models.CharField(
        max_length=20,
        choices=ADMISSION_STATUS,
        default='pending'
    )

   

    def save(self, *args, **kwargs):
        if not self.admission_no:
            with transaction.atomic():  
                self.admission_no = self.generate_admission_no()
        super().save(*args, **kwargs)

    def generate_admission_no(self):
        with transaction.atomic():
            last_admission = Admission.objects.select_for_update().last()  # Lock the row
            if last_admission:
                return f"ADM{int(last_admission.admission_no[3:]) + 1:04d}"
            return "ADM0001"
    def __str__(self):
        return self.full_name


# class PersonalInfo(TimeStampedModel):
#     """
#     Stores personal information about the student, including their full name,
#     date of birth, contact details, health information, and identification
#     marks.
#     """
#     full_name = models.CharField(
#         max_length=150,
#         verbose_name="Full Name",
#         help_text="Enter the full name of the individual.",
#     )
#     date_of_birth = models.DateField(
#         verbose_name="Date of Birth", help_text="Enter the date of birth."
#     )
#     gender = models.CharField(
#         max_length=6,
#         choices=GENDER_CHOICES,
#         verbose_name="Gender",
#         help_text="Select the gender.",
#     )
#     blood_group = models.CharField(
#         max_length=3,
#         choices=BLOOD_GROUP_CHOICES,
#         verbose_name="Blood Group",
#         help_text="Select the blood group.",
#     )
#     place_of_birth = models.CharField(
#         max_length=128,
#         verbose_name="Place of Birth",
#         help_text="Enter the place of birth.",
#     )
#     current_address = models.CharField(
#         max_length=255,
#         verbose_name="Current Address",
#         help_text="Enter the current address.",
#     )
#     permanent_address = models.CharField(
#         max_length=255,
#         verbose_name="Permanent Address",
#         help_text="Enter the permanent address.",
#     )
#     mobile_number = models.CharField(
#         max_length=11,
#         validators=[
#             RegexValidator(
#                 r"^\d{11}$", "Enter a valid 11-digit mobile number."
#             )
#         ],
#         verbose_name="Mobile Number",
#         help_text="Enter an 11-digit mobile number.",
#     )
#     email = models.EmailField(
#         verbose_name="Email Address", help_text="Enter a valid email address."
#     )
#     general_health = models.CharField(
#         max_length=50,
#         choices=HEALTH_CHOICES,
#         verbose_name="General Health Status",
#         help_text="Select general health status.",
#     )
#     immunization = models.CharField(
#         max_length=50,
#         choices=IMMUNIZATION_CHOICES,
#         verbose_name="Immunization Status",
#         help_text="Select immunization status.",
#     )
#     disabilities = models.CharField(
#         max_length=255,
#         blank=True,
#         null=True,
#         verbose_name="Disabilities",
#         help_text="Enter any known disabilities, if any.",
#     )
#     mark_of_identification = models.CharField(
#         max_length=255,
#         blank=True,
#         null=True,
#         verbose_name="Mark of Identification",
#         help_text="Enter any identifying marks, if any.",
#     )
#     # Added missing fields from the original model
#     child = models.CharField(  # Assuming this refers to the child's name 
#         max_length=100,
#         blank=True,
#         null=True,
#         verbose_name="Child's Name",
#         help_text="Enter the child's full name (if applicable).",
#     )
#     form_b_no = models.CharField(
#         max_length=50,
#         blank=True,
#         null=True,
#         verbose_name="Form B Number",
#         help_text="Enter the Form B number (if applicable).",
#     )
#     phone_residence = models.CharField(
#         max_length=15,
#         blank=True,
#         null=True,
#         verbose_name="Residence Phone Number",
#         help_text="Enter the residence phone number.",
#     )
#     office_address = models.CharField(
#         max_length=255,
#         blank=True,
#         null=True,
#         verbose_name="Office Address",
#         help_text="Enter the office address.",
#     )

#     class Meta:
#         indexes = [
#             models.Index(fields=["full_name"], name="full_name_idx"),
#             models.Index(fields=["date_of_birth"], name="dob_idx"),
#         ]

#     def __str__(self):
#         return self.full_name







# class ParentInfo(TimeStampedModel):
#     """
#     Stores information about the parents of a student,
#     including their names, CNIC numbers, occupations, and contact details.
#     """
#     father_full_name = models.CharField(
#         max_length=100,
#         verbose_name="Father Full Name",
#         help_text="Enter the father's full name.",
#     )
#     father_cnic = models.CharField(
#         max_length=15,
#         validators=[validate_cnic],
#         verbose_name="Father's CNIC",
#         help_text="Enter the father's CNIC.",
#     )
#     father_occupation = models.ForeignKey(
#         'Occupation',
#         related_name="parentinfo_father_occupation",
#         on_delete=models.CASCADE,
#         verbose_name="Father's Occupation",
#         help_text="Select father's occupation.",
#     )
#     mother_full_name = models.CharField(
#         max_length=100,
#         verbose_name="Mother Full Name",
#         help_text="Enter the mother's full name.",
#     )
#     mother_cnic = models.CharField(
#         max_length=15,
#         validators=[validate_cnic],
#         verbose_name="Mother's CNIC",
#         help_text="Enter the mother's CNIC.",
#     )
#     mother_occupation = models.ForeignKey(
#         'Occupation',
#         related_name="parentinfo_mother_occupation",
#         on_delete=models.CASCADE,
#         verbose_name="Mother's Occupation",
#         help_text="Select mother's occupation.",
#     )
#     mother_mobile_number = models.CharField(
#         max_length=11,
#         validators=[
#             RegexValidator(
#                 r"^\d{11}$", "Enter a valid 11-digit mobile number."
#             )
#         ],
#         verbose_name="Mother's Mobile Number",
#         help_text="Enter the mother's 11-digit mobile number.",
#     )
#     mother_email = models.EmailField(
#         verbose_name="Mother's Email Address",
#         help_text="Enter a valid email address.",
#     )
#     mother_office_address = models.CharField(
#         max_length=255,
#         verbose_name="Mother's Office Address",
#         help_text="Enter the mother's office address.",
#     )
#     mother_is_alive = models.BooleanField(
#         default=True,
#         verbose_name="Is Mother Alive?",
#         help_text="Indicates if the mother is alive.",
#     )

#     class Meta:
#         indexes = [
#             models.Index(fields=["father_full_name"], name="father_name_idx"),
#             models.Index(fields=["mother_full_name"], name="mother_name_idx"),
#         ]

#     def __str__(self):
#         return f"{self.father_full_name} - {self.mother_full_name}"


# class GuardianInfo(TimeStampedModel):
#     """
#     Stores information about the guardian of a student, including their
#     name, CNIC number, occupation, contact details, and relationship to the 
#     child.
#     """
#     full_name = models.CharField(
#         max_length=100,
#         verbose_name="Guardian Full Name",
#         help_text="Enter the guardian's full name.",
#     )
#     cnic = models.CharField(
#         max_length=15,
#         validators=[validate_cnic],
#         verbose_name="Guardian's CNIC",
#         help_text="Enter the guardian's CNIC.",
#     )
#     occupation = models.ForeignKey(
#         'Occupation',
#         on_delete=models.SET_NULL,  # Changed to SET_NULL to handle occupation deletion
#         null=True,
#         blank=True,
#         verbose_name="Guardian's Occupation",
#         help_text="Select guardian's occupation.",
#     )
#     mobile_number = models.CharField(
#         max_length=11,
#         blank=True,
#         null=True,
#         validators=[
#             RegexValidator(
#                 r"^\d{11}$", "Enter a valid 11-digit mobile number."
#             )
#         ],
#         verbose_name="Guardian's Mobile Number",
#         help_text="Enter the guardian's 11-digit mobile number.",
#     )
#     email = models.EmailField(
#         blank=True,
#         null=True,
#         verbose_name="Guardian's Email Address",
#         help_text="Enter a valid email address.",
#     )
#     home_address = models.CharField(
#         max_length=255,
#         blank=True,
#         null=True,
#         verbose_name="Guardian's Home Address",
#         help_text="Enter the guardian's home address.",
#     )
#     office_address = models.CharField(
#         max_length=255,
#         blank=True,
#         null=True,
#         verbose_name="Guardian's Office Address",
#         help_text="Enter the guardian's office address.",
#     )
#     relation_to_child = models.CharField(
#         max_length=50,
#         choices=GUARDIAN_RELATION_CHOICES,  # Added choices for guardian relation
#         verbose_name="Guardian's Relation to Child",
#         help_text="Enter the guardian's relation to the child.",
#     )
#     # Added missing fields from the original model
#     pick_and_drop = models.CharField(
#         max_length=20,
#         choices=PICK_N_DROP_CHOICES,
#         verbose_name="Pick and Drop",
#         help_text="Select if the child needs pick and drop service.",
#     )
#     pick_and_drop_by = models.CharField(
#         max_length=100,
#         blank=True,
#         null=True,
#         verbose_name="Pick and Drop By",
#         help_text="Enter the name of the person responsible for pick and drop.",
#     )
#     pick_and_drop_cnic = models.CharField(
#         max_length=15,
#         blank=True,
#         null=True,
#         validators=[validate_cnic],
#         verbose_name="Pick and Drop CNIC",
#         help_text="Enter the CNIC of the person responsible for pick and drop.",
#     )

#     class Meta:
#         indexes = [
#             models.Index(fields=["full_name"], name="guardian_name_idx"),
#         ]

#     def __str__(self):
#         return self.full_name











# class AcademicInfo(TimeStampedModel):
#     """
#     Stores admission-related academic details like the class and section the 
#     student is admitted into, their previous academic records, and enrollment 
#     status.
#     """
#     admission_class = models.ForeignKey(
#         'academic.Class', 
#         on_delete=models.CASCADE, 
#         related_name='admitted_class', 
#         verbose_name="Admission Class"
#     )
#     admission_section = models.ForeignKey(
#         'academic.Section', 
#         on_delete=models.CASCADE, 
#         verbose_name="Admission Section"
#     )
#     admission_no = models.CharField(
#         max_length=12, 
#         unique=True, 
#         blank=True, 
#         null=True, 
#         verbose_name="Admission Number", 
#         help_text="Unique admission number for the student"
#     )
#     admission_type = models.CharField(
#         max_length=50, 
#         choices=ADMISSION_TYPE_CHOICES, 
#         verbose_name="Admission Type", 
#         help_text="Type of admission (New/Transfer)"
#     )
#     admission_confirmation_date = models.DateField(
#         null=True, 
#         blank=True, 
#         verbose_name="Admission Confirmation Date", 
#         help_text="Date when admission was confirmed"
#     )
#     marks_in_previous_school = models.PositiveIntegerField(
#         null=True, 
#         blank=True, 
#         verbose_name="Marks in Previous School", 
#         help_text="Marks obtained in previous school"
#     )
#     previous_school_roll_no = models.CharField(
#         max_length=20, 
#         blank=True, 
#         null=True, 
#         verbose_name="Previous School Roll No", 
#         help_text="Roll number in the previous school"
#     )
#     enrollment_status = models.CharField(
#         max_length=50, 
#         choices=ENROLLMENT_CHOICES, 
#         verbose_name="Enrollment Status", 
#         help_text="Current enrollment status of the student"
#     )
#     test_passed = models.BooleanField(
#         default=False, 
#         verbose_name="Test Passed", 
#         help_text="Indicates whether the admission test was passed"
#     )
#     # Added missing field from the original model
#     class_required = models.ForeignKey(
#         'academic.Class', 
#         on_delete=models.CASCADE, 
#         related_name='required_class', 
#         verbose_name="Class Required"
#     )

#     class Meta:
#         indexes = [
#             models.Index(fields=['admission_no'], name='admission_no_idx'),
#             models.Index(
#                 fields=['admission_confirmation_date'], 
#                 name='adm_conf_date_idx'
#             ),
#         ]

#     def save(self, *args, **kwargs):
#         if not self.admission_no:
#             # Use a transaction for thread safety when generating admission_no
#             with transaction.atomic():  
#                 self.admission_no = self.generate_admission_no()
#         super().save(*args, **kwargs)

#     def generate_admission_no(self):
#         last_admission = AcademicInfo.objects.select_for_update().last()
#         if last_admission:
#             return f"ADM{int(last_admission.admission_no[3:]) + 1:04d}"
#         return "ADM0001"

#     def __str__(self):
#         return f"{self.admission_class} - {self.admission_section}"









# class FinancialInfo(TimeStampedModel):
#     """
#     Stores financial information related to the student's admission, including 
#     fee details, payment schedules, and any outstanding dues.
#     """
#     category = models.ForeignKey(
#         'common.Category', 
#         on_delete=models.PROTECT, 
#         verbose_name="Category"
#     )
#     fee_remaining_for_months = models.PositiveIntegerField(
#         null=True, 
#         blank=True, 
#         verbose_name="Fee Remaining for Months (if any)", 
#         help_text="Number of months with remaining fees"
#     )
#     monthly_income = models.PositiveIntegerField(
#         null=True, 
#         blank=True, 
#         verbose_name="Monthly Income", 
#         help_text="Monthly income of the guardian"
#     )
#     paid_dues_upto_slc = models.DateField(
#         null=True, 
#         blank=True, 
#         verbose_name="Paid Dues up to School Leaving Certificate", 
#         help_text="Date of paid dues up to the SLC"
#     )
#     # Added missing fields from the original model
#     advance = models.PositiveIntegerField(
#         default=0, 
#         verbose_name="Advance Payment"
#     )
#     arrears = models.PositiveIntegerField(
#         default=0, 
#         verbose_name="Arrears"
#     )
#     total_arrear_months = models.PositiveIntegerField(
#         default=0, 
#         verbose_name="Total Arrear Months"
#     )

#     class Meta:
#         indexes = [
#             models.Index(
#                 fields=['paid_dues_upto_slc'], 
#                 name='paid_dues_upto_slc_idx'
#             ),
#         ]

#     def __str__(self):
#         return str(self.category)








# class AdditionalInfo(TimeStampedModel):
#     """
#     Stores additional information related to the student's admission, such as 
#     nationality, religion, extracurricular activities, sibling details, and 
#     remarks.
#     """
#     nationality = models.ForeignKey(
#         'common.Nationality', 
#         on_delete=models.SET_NULL, 
#         null=True
#     )
#     religion = models.ForeignKey(
#         'common.Religion', 
#         on_delete=models.SET_NULL, 
#         null=True
#     )
#     extra_act = models.TextField(
#         blank=True, 
#         null=True, 
#         verbose_name="Extracurricular Activities", 
#         help_text="Details of extracurricular activities"
#     )
#     sibling = models.TextField(
#         blank=True, 
#         null=True, 
#         verbose_name="Sibling Information", 
#         help_text="Information about siblings"
#     )
#     remarks = models.TextField(
#         blank=True, 
#         null=True, 
#         verbose_name="Remarks", 
#         help_text="Any additional remarks"
#     )
#     is_alive = models.BooleanField(
#         default=True, 
#         verbose_name="Is Alive", 
#         help_text="Indicates if the student is alive"
#     )
#     is_security_voucher_generated = models.BooleanField(
#         default=False, 
#         verbose_name="Security Voucher Generated", 
#         help_text="Indicates if a security voucher has been generated"
#     )
#     is_voucher_generated = models.BooleanField(default=False, verbose_name="Voucher Generated", help_text="Indicates if a voucher has been generated")
#     # Added missing fields from the original model
#     admission_by = models.CharField(
#         max_length=100, verbose_name="Admitted By"
#     )
#     other_information = models.TextField(
#         blank=True, 
#         null=True, 
#         verbose_name="Other Information"
#     )

#     class Meta:
#         indexes = [
#             models.Index(fields=['nationality'], name='nationality_idx'),
#         ]

#     def __str__(self):
#         return f"{self.religion} - {self.nationality}"



















































