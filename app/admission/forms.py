# admission/forms.py
from django import forms
from .models import PersonalInfo, ParentInfo, AcademicInfo, FinancialInfo, AdditionalInfo, Admission

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = '__all__'  # Include all fields from PersonalInfo

class ParentInfoForm(forms.ModelForm):
    class Meta:
        model = ParentInfo
        fields = '__all__'

class AcademicInfoForm(forms.ModelForm):
    class Meta:
        model = AcademicInfo
        fields = '__all__'

class FinancialInfoForm(forms.ModelForm):
    class Meta:
        model = FinancialInfo
        fields = '__all__'

class AdditionalInfoForm(forms.ModelForm):
    class Meta:
        model = AdditionalInfo
        fields = '__all__'

class AdmissionForm(forms.ModelForm):
    # These fields will be gathered in one form
    class Meta:
        model = Admission
        fields = ['admission_by', 'admission_no', 'admission_confirmation_date', 'admission_type']
