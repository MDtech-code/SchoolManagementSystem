from django.shortcuts import render, redirect
from .forms import PersonalInfoForm, ParentInfoForm, AcademicInfoForm, FinancialInfoForm, AdditionalInfoForm, AdmissionForm
from django.db import transaction

def create_admission(request):
    if request.method == 'POST':
        personal_info_form = PersonalInfoForm(request.POST)
        parent_info_form = ParentInfoForm(request.POST)
        academic_info_form = AcademicInfoForm(request.POST)
        financial_info_form = FinancialInfoForm(request.POST)
        additional_info_form = AdditionalInfoForm(request.POST)
        admission_form = AdmissionForm(request.POST)

        if all([personal_info_form.is_valid(), parent_info_form.is_valid(), 
                academic_info_form.is_valid(), financial_info_form.is_valid(),
                additional_info_form.is_valid(), admission_form.is_valid()]):
            
            with transaction.atomic():
                # Save each form
                personal_info = personal_info_form.save()
                parent_info = parent_info_form.save()
                academic_info = academic_info_form.save()
                financial_info = financial_info_form.save()
                additional_info = additional_info_form.save()

                # Create Admission record and link the sub-models
                admission = admission_form.save(commit=False)
                admission.personal_info = personal_info
                admission.parent_info = parent_info
                admission.academic_info = academic_info
                admission.financial_info = financial_info
                admission.additional_info = additional_info
                admission.save()

            return redirect('admission_success')  # Redirect to success page
    else:
        # Initialize empty forms
        personal_info_form = PersonalInfoForm()
        parent_info_form = ParentInfoForm()
        academic_info_form = AcademicInfoForm()
        financial_info_form = FinancialInfoForm()
        additional_info_form = AdditionalInfoForm()
        admission_form = AdmissionForm()

    return render(request, 'admission/create_admission.html', {
        'personal_info_form': personal_info_form,
        'parent_info_form': parent_info_form,
        'academic_info_form': academic_info_form,
        'financial_info_form': financial_info_form,
        'additional_info_form': additional_info_form,
        'admission_form': admission_form,
    })

