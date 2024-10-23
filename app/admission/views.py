from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import View
from .forms import PersonalInfoForm, ParentInfoForm, AcademicInfoForm, FinancialInfoForm, AdditionalInfoForm
from .models import Admission

class AdmissionCreateView(View):
    template_name = 'admission/create_admission.html'
    success_url = reverse_lazy('admission_success')  # Define your success URL

    def get(self, request, *args, **kwargs):
        # Initialize empty forms on GET request
        context = {
            'personal_info_form': PersonalInfoForm(),
            'parent_info_form': ParentInfoForm(),
            'academic_info_form': AcademicInfoForm(),
            'financial_info_form': FinancialInfoForm(),
            'additional_info_form': AdditionalInfoForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # Initialize forms with POST data
        personal_info_form = PersonalInfoForm(request.POST)
        parent_info_form = ParentInfoForm(request.POST)
        academic_info_form = AcademicInfoForm(request.POST)
        financial_info_form = FinancialInfoForm(request.POST)
        additional_info_form = AdditionalInfoForm(request.POST)

        if (personal_info_form.is_valid() and parent_info_form.is_valid() and 
            academic_info_form.is_valid() and financial_info_form.is_valid() and 
            additional_info_form.is_valid()):
            
            # Save each form instance
            personal_info = personal_info_form.save()
            parent_info = parent_info_form.save()
            academic_info = academic_info_form.save()
            financial_info = financial_info_form.save()
            additional_info = additional_info_form.save()

            # Create Admission record linking the saved form instances
            Admission.objects.create(
                personal_info=personal_info,
                parent_info=parent_info,
                academic_info=academic_info,
                financial_info=financial_info,
                additional_info=additional_info
            )
            
            # Redirect after successful submission
            return redirect(self.success_url)
        else:
            # If any form is invalid, re-render the form with errors
            context = {
                'personal_info_form': personal_info_form,
                'parent_info_form': parent_info_form,
                'academic_info_form': academic_info_form,
                'financial_info_form': financial_info_form,
                'additional_info_form': additional_info_form,
            }
            return render(request, self.template_name, context)
