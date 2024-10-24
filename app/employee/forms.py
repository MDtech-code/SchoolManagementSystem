#from django import forms
#from .models import Employee
#
#class EmployeeForm(forms.ModelForm):
#    class Meta:
#        model = Employee
#        fields = '__all__'
#        widgets = {
#            'city':forms.TextInput(attrs={'class':'form-control'})
#       }
#
#

from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'employee_name', 'employee_id', 'designation', 'employee_pay_structure', 'account_no', 'address',
            'bank', 'city', 'cnic', 'contact_no', 'country', 'covid_vaccinated', 'date_of_birth', 'date_of_joining',
            'date_of_rejoining', 'date_of_resignation', 'email', 'employee_status', 'father_cnic', 'father_name',
            'gender', 'is_verified', 'martial_status', 'province', 'wing'
        ]
        widgets = {
            'employee_name': forms.TextInput(attrs={'class': 'form-control'}),
            'employee_id': forms.TextInput(attrs={'class': 'form-control'}),
            'designation': forms.Select(attrs={'class': 'form-control'}),
            'employee_pay_structure': forms.Select(attrs={'class': 'form-control'}),
            'account_no': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'bank': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'cnic': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_no': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'covid_vaccinated': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_of_joining': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_of_rejoining': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_of_resignation': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'employee_status': forms.TextInput(attrs={'class': 'form-control'}),
            'father_cnic': forms.TextInput(attrs={'class': 'form-control'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(choices=[('Male', 'Male'), ('Female', 'Female')], attrs={'class': 'form-control'}),
            'is_verified': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'martial_status': forms.Select(choices=[('Single', 'Single'), ('Married', 'Married')], attrs={'class': 'form-control'}),
            'province': forms.TextInput(attrs={'class': 'form-control'}),
            'wing': forms.TextInput(attrs={'class': 'form-control'}),
        }


