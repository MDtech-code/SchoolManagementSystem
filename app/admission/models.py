'''
from django.db import models
from app.common.models import TimeStampedModel
from app.fee.models import Category
from app.academic.models import Class,Section






class Religion(TimeStampedModel,models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name}"
    

class Nationality(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.title}"
    

class Province(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.title}"





#! Stores personal information about the student

class PersonalInfo(TimeStampedModel,models.Model):
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=3)
    place_of_birth = models.CharField(max_length=100)
    current_address = models.CharField(max_length=255)
    permanent_address = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField()
    general_health = models.CharField(max_length=255)
    immunization = models.CharField(max_length=255)
    disabilities = models.CharField(max_length=255)
    mark_of_identification = models.CharField(max_length=255)

#! Stores parent/guardian information
class ParentInfo(TimeStampedModel,models.Model):
    father_full_name = models.CharField(max_length=100)
    father_cnic = models.CharField(max_length=15)
    father_occupation = models.ForeignKey(Category, related_name='father_occupation', on_delete=models.CASCADE)
    mother_full_name = models.CharField(max_length=100)
    mother_cnic = models.CharField(max_length=15)
    mother_occupation = models.ForeignKey(Category, related_name='mother_occupation', on_delete=models.CASCADE)
    mother_mobile_number = models.CharField(max_length=15)
    mother_email = models.EmailField()
    mother_office_address = models.CharField(max_length=255)
    guardian_full_name = models.CharField(max_length=100)
    guardian_cnic = models.CharField(max_length=15)
    guardian_occupation = models.ForeignKey(Category, related_name='guardian_occupation', on_delete=models.CASCADE)
    guardian_mobile_number = models.CharField(max_length=15)
    guardian_email = models.EmailField()
    guardian_home_address = models.CharField(max_length=255)
    guardian_office_address = models.CharField(max_length=255)
    guardian_relation_to_child = models.CharField(max_length=50)


#! Stores admission-related academic details like the class and section the student is admitted into.
class AcademicInfo(TimeStampedModel,models.Model):
    admission_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    admission_section = models.ForeignKey(Section, on_delete=models.CASCADE)
    admission_no = models.CharField(max_length=20)
    admission_type = models.CharField(max_length=50)
    admission_confirmation_date = models.DateField()
    marks_in_previous_school = models.PositiveIntegerField()
    previous_school_roll_no = models.CharField(max_length=20)
    enrollment_status = models.CharField(max_length=50)
    test_passed = models.BooleanField(default=False)

#! Tracks any admission fees and initial payments.
class FinancialInfo(TimeStampedModel,models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    fee_remaining_for_months = models.PositiveIntegerField()
    monthly_income = models.PositiveIntegerField()
    paid_dues_upto_slc = models.DateField()


#! Handles miscellaneous data like religion, nationality, etc.
class AdditionalInfo(TimeStampedModel,models.Model):
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
class Admission(TimeStampedModel,models.Model):
    personal_info = models.OneToOneField(PersonalInfo, on_delete=models.CASCADE)
    parent_info = models.OneToOneField(ParentInfo, on_delete=models.CASCADE)
    academic_info = models.OneToOneField(AcademicInfo, on_delete=models.CASCADE)
    financial_info = models.OneToOneField(FinancialInfo, on_delete=models.CASCADE)
    additional_info = models.OneToOneField(AdditionalInfo, on_delete=models.CASCADE)
    admission_by = models.CharField(max_length=100)
    admission_confirmation_date = models.DateField()
    admission_no = models.CharField(max_length=20)
    admission_type = models.CharField(max_length=50)
   
    def __str__(self):
        return self.personal_info.full_name

'''

'''
class Admission(models.Model):
    admission_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    admission_section = models.ForeignKey(Section, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    class_required = models.ForeignKey(Class, related_name='required_class', on_delete=models.CASCADE)
    father_occupation = models.ForeignKey(Category, related_name='father_occupation', on_delete=models.CASCADE)
    guardian_occupation = models.ForeignKey(Category, related_name='guardian_occupation', on_delete=models.CASCADE)
    mother_occupation = models.ForeignKey(Category, related_name='mother_occupation', on_delete=models.CASCADE)
    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE)
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE)
    admission_by = models.CharField(max_length=100)
    admission_confirmation_date = models.DateField()
    admission_no = models.CharField(max_length=20)
    admission_type = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=3)
    child = models.CharField(max_length=100)
    computer = models.PositiveIntegerField()
    current_address = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    disabilities = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    email = models.EmailField()
    english = models.PositiveIntegerField()
    enrollment_status = models.CharField(max_length=50)
    extra_act = models.CharField(max_length=255)
    father_cnic = models.CharField(max_length=15)
    father_full_name = models.CharField(max_length=100)
    fee_remaining_for_months = models.PositiveIntegerField()
    form_b_no = models.CharField(max_length=15)
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    general_health = models.CharField(max_length=255)
    guardian_cnic = models.CharField(max_length=15)
    guardian_email = models.EmailField()
    guardian_full_name = models.CharField(max_length=100)
    guardian_home_address = models.CharField(max_length=255)
    guardian_mobile_number = models.CharField(max_length=15)
    guardian_office_address = models.CharField(max_length=255)
    guardian_relation_to_child = models.CharField(max_length=50)
    immunization = models.CharField(max_length=255)
    is_alive = models.BooleanField(default=True)
    is_security_voucher_generated = models.BooleanField(default=False)
    is_voucher_generated = models.BooleanField(default=False)
    islamiat = models.PositiveIntegerField()
    mark_of_identification = models.CharField(max_length=255)
    marks_in_previous_school = models.PositiveIntegerField()
    maths = models.PositiveIntegerField()
    mobile_number = models.CharField(max_length=15)
    monthly_income = models.PositiveIntegerField()
    mother_cnic = models.CharField(max_length=15)
    mother_education = models.CharField(max_length=255)
    mother_email = models.EmailField()
    mother_full_name = models.CharField(max_length=100)
    mother_is_alive = models.BooleanField(default=True)
    mother_mobile_number = models.CharField(max_length=15)
    mother_office_address = models.CharField(max_length=255)
    mother_office_phone = models.CharField(max_length=15)
    office_address = models.CharField(max_length=255)
    other_information = models.CharField(max_length=255)
    paid_dues_upto_slc = models.DateField()
    permanent_address = models.CharField(max_length=255)
    phone_residence = models.CharField(max_length=15)
    pick_and_drop = models.CharField(max_length=255)
    pick_and_drop_by = models.CharField(max_length=100)
    pick_and_drop_cnic = models.CharField(max_length=15)
    place_of_birth = models.CharField(max_length=100)
    previous_school_roll_no = models.CharField(max_length=20)
    rank = models.CharField(max_length=50)
    remarks = models.TextField()
    school_address = models.CharField(max_length=255)
    school_name = models.CharField(max_length=100)
    science = models.PositiveIntegerField()
    sibling = models.TextField()
    student_id = models.CharField(max_length=20)
    test_passed = models.BooleanField(default=False)
    urdu = models.PositiveIntegerField()

    def __str__(self):
        return self.full_name
'''