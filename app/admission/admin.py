# admission/admin.py

from django.contrib import admin
from .models import (
    PersonalInfo,
    ParentInfo,
    AcademicInfo,
    FinancialInfo,
    AdditionalInfo,
    Admission,
    
)

# Admin classes for better presentation and functionality
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'date_of_birth', 'gender', 'mobile_number', 'email')
    search_fields = ('full_name', 'email')
    list_filter = ('gender', 'blood_group')

class ParentInfoAdmin(admin.ModelAdmin):
    list_display = ('father_full_name', 'mother_full_name', 'guardian_full_name', 'father_cnic')
    search_fields = ('father_full_name', 'mother_full_name', 'guardian_full_name')
    list_filter = ('father_occupation', 'mother_occupation')

class AcademicInfoAdmin(admin.ModelAdmin):
    list_display = ('admission_no', 'admission_class', 'admission_section', 'marks_in_previous_school')
    search_fields = ('admission_no',)
    list_filter = ('admission_class', 'admission_section', 'test_passed')

class FinancialInfoAdmin(admin.ModelAdmin):
    list_display = ('category', 'fee_remaining_for_months', 'monthly_income')
    search_fields = ('category__name',)  # Assuming Category has a name field

class AdditionalInfoAdmin(admin.ModelAdmin):
    list_display = ('religion', 'nationality', 'is_alive')
    search_fields = ('sibling', 'other_information')

class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('admission_no', 'personal_info', 'admission_confirmation_date', 'admission_type')
    search_fields = ('admission_no', 'personal_info__full_name')
    list_filter = ('admission_type', 'admission_confirmation_date')

# Registering the models with the admin site
admin.site.register(PersonalInfo, PersonalInfoAdmin)
admin.site.register(ParentInfo, ParentInfoAdmin)
admin.site.register(AcademicInfo, AcademicInfoAdmin)
admin.site.register(FinancialInfo, FinancialInfoAdmin)
admin.site.register(AdditionalInfo, AdditionalInfoAdmin)
admin.site.register(Admission, AdmissionAdmin)


