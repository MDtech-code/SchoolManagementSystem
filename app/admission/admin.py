from django.contrib import admin
from .models import (
    PersonalInfo,
    Occupation,
    ParentInfo,
    GuardianInfo,
    AcademicInfo,
    FinancialInfo,
    AdditionalInfo
)


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ("full_name", "date_of_birth", "gender", "blood_group", "mobile_number")
    search_fields = ("full_name", "mobile_number")
    list_filter = ("gender", "blood_group")
    readonly_fields = ("created_at", "updated_at")


@admin.register(Occupation)
class OccupationAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(ParentInfo)
class ParentInfoAdmin(admin.ModelAdmin):
    list_display = ("father_full_name", "father_cnic", "mother_full_name", "mother_cnic")
    search_fields = ("father_full_name", "mother_full_name")
    readonly_fields = ("created_at", "updated_at")


@admin.register(GuardianInfo)
class GuardianInfoAdmin(admin.ModelAdmin):
    list_display = ("full_name", "cnic", "relation_to_child", "mobile_number")
    search_fields = ("full_name", "cnic")
    list_filter = ("relation_to_child",)
    readonly_fields = ("created_at", "updated_at")


@admin.register(AcademicInfo)
class AcademicInfoAdmin(admin.ModelAdmin):
    list_display = ("admission_class", "admission_section", "admission_no", "admission_type", "enrollment_status")
    search_fields = ("admission_no",)
    list_filter = ("admission_type", "enrollment_status")
    readonly_fields = ("created_at", "updated_at")
    # Prevent editing admission_no directly
    exclude = ("admission_no",)


@admin.register(FinancialInfo)
class FinancialInfoAdmin(admin.ModelAdmin):
    list_display = ("category", "fee_remaining_for_months", "monthly_income", "paid_dues_upto_slc")
    search_fields = ("category__name",)
    readonly_fields = ("created_at", "updated_at")


@admin.register(AdditionalInfo)
class AdditionalInfoAdmin(admin.ModelAdmin):
    list_display = ("nationality", "religion")
    readonly_fields = ("created_at", "updated_at")


