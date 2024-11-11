from django import forms
from .models import Admission

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        exclude = ['applicant', 'admission_status', 'admission_no','is_voucher_generated','is_security_voucher_generated']  # Exclude fields not to be filled by the user
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'paid_dues_upto_slc': forms.DateInput(attrs={'type': 'date'}),
            'admission_confirmation_date': forms.DateInput(attrs={'type': 'date'}),
        }
        def __init__(self, *args, **kwargs):
            super(AdmissionForm, self).__init__(*args, **kwargs)
        
        # Add Bootstrap classes to all form fields
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['placeholder'] = field.label