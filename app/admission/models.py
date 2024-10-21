
from django.db import models
from app.common.models import TimeStampedModel,Category,Religion,Nationality
from app.academic.models import Class,Section
from django.core.exceptions import ValidationError
from core.utils.choices import GENDER_CHOICES, BLOOD_GROUP_CHOICES, PICK_N_DROP_CHOICES, CHILD_CHOICES, \
    HEALTH_CHOICES, IMMUNIZATION_CHOICES, GUARDIAN_RELATION_CHOICES, ENROLLMENT_CHOICES, \
    STUDENT_STATUS_CHOICES, ADMISSION_TYPE_CHOICES, VOUCHER_TYPE_CHOICES, SUBJECT_CHOICE


#! Stores personal information about the student

class PersonalInfo(TimeStampedModel):
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    blood_group = models.CharField(choices=BLOOD_GROUP_CHOICES,max_length=3)
    place_of_birth = models.CharField(max_length=128)
    current_address = models.CharField(max_length=255)
    permanent_address = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField()
    general_health = models.CharField(choices=HEALTH_CHOICES,max_length=255)
    immunization = models.CharField(choices=IMMUNIZATION_CHOICES,max_length=255)
    disabilities = models.CharField(max_length=255)
    mark_of_identification = models.CharField(max_length=255)

#! Stores parent/guardian information
class Occupation(models.Model):
    name = models.CharField(max_length=100)  # e.g., Doctor, Engineer, etc.
    
    def __str__(self):
        return self.name
    

def validate_cnic(value):
    # Remove any hyphens
    if value:
        cleaned = value.replace('-', '')

        # Check if it's all digits and has a length of 13
        if not cleaned.isdigit() or len(cleaned) != 13:
            raise ValidationError('CNIC must have 13 digits.')

        # If the original value doesn't have hyphens, insert them
        if '-' not in value:
            value = f"{cleaned[:5]}-{cleaned[5:12]}-{cleaned[12]}"

    return value

class ParentInfo(TimeStampedModel):
    father_full_name = models.CharField(max_length=100, verbose_name="Father Full Name")
    father_cnic = models.CharField(max_length=15, verbose_name="CNIC")
    father_occupation = models.ForeignKey(Occupation, related_name='parentinfo_father_occupation', on_delete=models.CASCADE)
    mother_full_name = models.CharField(max_length=100, verbose_name="Mother Full Name") 
    mother_cnic = models.CharField(max_length=15, verbose_name="CNIC")
    mother_occupation = models.ForeignKey(Occupation, related_name='parentinfo_mother_occupation', on_delete=models.CASCADE)
    mother_mobile_number = models.CharField(max_length=15)
    mother_email = models.EmailField()
    mother_office_address = models.CharField(max_length=255)
    guardian_full_name = models.CharField(max_length=100, verbose_name="guardian Full Name")
    guardian_cnic = models.CharField(max_length=15, verbose_name="CNIC")
    guardian_occupation = models.ForeignKey(Occupation, related_name='parentinfo_guardian_occupation', on_delete=models.CASCADE)
    guardian_mobile_number = models.CharField(max_length=15)
    guardian_email = models.EmailField()
    guardian_home_address = models.CharField(max_length=255)
    guardian_office_address = models.CharField(max_length=255)
    guardian_relation_to_child = models.CharField(max_length=50)


#! Stores admission-related academic details like the class and section the student is admitted into.
class AcademicInfo(TimeStampedModel):
    admission_class = models.ForeignKey(Class, on_delete=models.CASCADE,related_name='admitted_class')
    admission_section = models.ForeignKey(Section, on_delete=models.CASCADE)
    admission_no = models.CharField(max_length=12)
    admission_type = models.CharField(max_length=50, choices=ADMISSION_TYPE_CHOICES)
    admission_confirmation_date = models.DateField()
    marks_in_previous_school = models.PositiveIntegerField()
    previous_school_roll_no = models.CharField(max_length=20)
    enrollment_status = models.CharField(max_length=50, choices=ENROLLMENT_CHOICES)
    test_passed = models.BooleanField(default=False)

#! Tracks any admission fees and initial payments.
class FinancialInfo(TimeStampedModel):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    fee_remaining_for_months = models.PositiveIntegerField()
    monthly_income = models.PositiveIntegerField()
    paid_dues_upto_slc = models.DateField()


#! Handles miscellaneous data like religion, nationality, etc.
class AdditionalInfo(TimeStampedModel):
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE)
    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE)
    extra_act = models.CharField(max_length=255)
    sibling = models.TextField()
    other_information = models.CharField(max_length=255)
    remarks = models.TextField()
    is_alive = models.BooleanField(default=True)
    is_security_voucher_generated = models.BooleanField(default=False)
    is_voucher_generated = models.BooleanField(default=False)


#! The central model that ties all the other models together for the admission process.
class Admission(TimeStampedModel):
    personal_info = models.OneToOneField(PersonalInfo, on_delete=models.CASCADE)
    parent_info = models.OneToOneField(ParentInfo, on_delete=models.CASCADE)
    academic_info = models.OneToOneField(AcademicInfo, on_delete=models.CASCADE)
    financial_info = models.OneToOneField(FinancialInfo, on_delete=models.CASCADE)
    additional_info = models.OneToOneField(AdditionalInfo, on_delete=models.CASCADE)
    admission_by = models.CharField(max_length=100)
    admission_confirmation_date = models.DateField()
    admission_no = models.CharField(max_length=20)
    admission_type = models.CharField(max_length=64, choices=ADMISSION_TYPE_CHOICES)
   
    def __str__(self):
        return self.personal_info.full_name



