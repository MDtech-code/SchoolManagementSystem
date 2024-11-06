from django import forms
from .models import PersonalInfo, ParentInfo, AcademicInfo, FinancialInfo, AdditionalInfo, GuardianInfo

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = '__all__'  # Or specify the fields you want in the form

class ParentInfoForm(forms.ModelForm):
    class Meta:
        model = ParentInfo
        fields = '__all__'  # Or specify the fields

class AcademicInfoForm(forms.ModelForm):
    class Meta:
        model = AcademicInfo
        fields = '__all__'  # Or specify the fields

class FinancialInfoForm(forms.ModelForm):
    class Meta:
        model = FinancialInfo
        fields = '__all__'  # Or specify the fields

class AdditionalInfoForm(forms.ModelForm):
    class Meta:
        model = AdditionalInfo
        fields = '__all__'  # Or specify the fields

class GuardianInfoForm(forms.ModelForm):
    class Meta:
        model = GuardianInfo
        fields = '__all__'  # Or specify the fields

'''
from django import forms
from .models import PersonalInfo, ParentInfo, AcademicInfo, FinancialInfo, AdditionalInfo

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = ['full_name', 'date_of_birth', 'gender', 'blood_group', 'place_of_birth', 'current_address', 'permanent_address', 'mobile_number', 'email', 'general_health', 'immunization', 'disabilities', 'mark_of_identification']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

class ParentInfoForm(forms.ModelForm):
    class Meta:
        model = ParentInfo
        fields = ['father_full_name', 'father_cnic', 'father_occupation', 'mother_full_name', 'mother_cnic', 'mother_occupation', 'mother_mobile_number', 'mother_email', 'guardian_full_name', 'guardian_cnic', 'guardian_occupation', 'guardian_mobile_number']

class AcademicInfoForm(forms.ModelForm):
    class Meta:
        model = AcademicInfo
        fields = ['admission_class', 'admission_section', 'admission_no', 'admission_type', 'admission_confirmation_date', 'marks_in_previous_school']
        widgets = {
            'admission_confirmation_date': forms.DateInput(attrs={'type': 'date'}),
        }

class FinancialInfoForm(forms.ModelForm):
    class Meta:
        model = FinancialInfo
        fields = ['category', 'fee_remaining_for_months', 'monthly_income', 'paid_dues_upto_slc']
        widgets = {
            'paid_dues_upto_slc': forms.DateInput(attrs={'type': 'date'}),
        }

class AdditionalInfoForm(forms.ModelForm):
    class Meta:
        model = AdditionalInfo
        fields = ['religion', 'nationality', 'extra_act', 'sibling', 'remarks', 'is_alive']






'''