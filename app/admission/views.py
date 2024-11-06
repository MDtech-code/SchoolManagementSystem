# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from django.db import transaction
# from .models import Admission, PersonalInfo, ParentInfo, AcademicInfo, FinancialInfo, AdditionalInfo, GuardianInfo
# from .forms import (
#     PersonalInfoForm,
#     ParentInfoForm,
#     AcademicInfoForm,
#     FinancialInfoForm,
#     AdditionalInfoForm,
#     GuardianInfoForm,
# )

# @login_required
# def initiate_admission(request):
#     """
#     View to handle the multi-step admission process.
#     """
#     # Use try-except blocks to handle cases where the related objects don't exist
#     try:
#         admission = Admission.objects.get(applicant=request.user)
#         personal_info = admission.personal_info
#         parent_info = admission.parent_info
#         academic_info = admission.academic_info
#         financial_info = admission.financial_info
#         additional_info = admission.additional_info
#         guardian_info = admission.guardian_info
#     except Admission.DoesNotExist:
#         admission = None
#         personal_info = None
#         parent_info = None
#         academic_info = None
#         financial_info = None
#         additional_info = None
#         guardian_info = None

#     if request.method == 'POST':
#         # Determine which form was submitted based on the button clicked
#         if 'personal_info_submit' in request.POST:
#             personal_info_form = PersonalInfoForm(request.POST, instance=personal_info)
#             if personal_info_form.is_valid():
#                 personal_info = personal_info_form.save(commit=False)
#                 # ... (any additional logic for personal_info) ...
#                 personal_info.save()
#                 messages.success(request, 'Personal information saved!')
#                 # If admission object doesn't exist, create it and link personal_info
#                 if not admission:
#                     admission = Admission.objects.create(applicant=request.user, personal_info=personal_info)
#                 else:
#                     admission.personal_info = personal_info
#                     admission.save()
#         elif 'parent_info_submit' in request.POST:
#             parent_info_form = ParentInfoForm(request.POST, instance=parent_info)
#             if parent_info_form.is_valid():
#                 parent_info = parent_info_form.save(commit=False)
#                 # ... (any additional logic for parent_info) ...
#                 parent_info.save()
#                 messages.success(request, 'Parent information saved!')
#                 if not admission:
#                     admission = Admission.objects.create(applicant=request.user, parent_info=parent_info)
#                 else:
#                     admission.parent_info = parent_info
#                     admission.save()
#         # ... (similarly handle other forms: academic_info, financial_info, etc.) ...

#         return redirect('initiate_admission')  # Redirect to the same view to refresh

#     else:  # GET request
#         personal_info_form = PersonalInfoForm(instance=personal_info)
#         parent_info_form = ParentInfoForm(instance=parent_info)
#         academic_info_form = AcademicInfoForm(instance=academic_info)
#         financial_info_form = FinancialInfoForm(instance=financial_info)
#         additional_info_form = AdditionalInfoForm(instance=additional_info)
#         guardian_info_form = GuardianInfoForm(instance=guardian_info)

#     context = {
#         'personal_info_form': personal_info_form,
#         'parent_info_form': parent_info_form,
#         'academic_info_form': academic_info_form,
#         'financial_info_form': financial_info_form,
#         'additional_info_form': additional_info_form,
#         'guardian_info_form': guardian_info_form,
#         'admission': admission,  # Pass the admission object to the template
#     }
#     return render(request, 'admission/initiate_admission.html', context)











# '''
# from django.shortcuts import redirect, render
# from django.urls import reverse_lazy
# from django.views.generic import View
# from .forms import PersonalInfoForm, ParentInfoForm, AcademicInfoForm, FinancialInfoForm, AdditionalInfoForm
# from .models import Admission

# class AdmissionCreateView(View):
#     template_name = 'admission/create_admission.html'
#     success_url = reverse_lazy('admission_success')  # Define your success URL

#     def get(self, request, *args, **kwargs):
#         # Initialize empty forms on GET request
#         context = {
#             'personal_info_form': PersonalInfoForm(),
#             'parent_info_form': ParentInfoForm(),
#             'academic_info_form': AcademicInfoForm(),
#             'financial_info_form': FinancialInfoForm(),
#             'additional_info_form': AdditionalInfoForm(),
#         }
#         return render(request, self.template_name, context)

#     def post(self, request, *args, **kwargs):
#         # Initialize forms with POST data
#         personal_info_form = PersonalInfoForm(request.POST)
#         parent_info_form = ParentInfoForm(request.POST)
#         academic_info_form = AcademicInfoForm(request.POST)
#         financial_info_form = FinancialInfoForm(request.POST)
#         additional_info_form = AdditionalInfoForm(request.POST)

#         if (personal_info_form.is_valid() and parent_info_form.is_valid() and 
#             academic_info_form.is_valid() and financial_info_form.is_valid() and 
#             additional_info_form.is_valid()):
            
#             # Save each form instance
#             personal_info = personal_info_form.save()
#             parent_info = parent_info_form.save()
#             academic_info = academic_info_form.save()
#             financial_info = financial_info_form.save()
#             additional_info = additional_info_form.save()

#             # Create Admission record linking the saved form instances
#             Admission.objects.create(
#                 personal_info=personal_info,
#                 parent_info=parent_info,
#                 academic_info=academic_info,
#                 financial_info=financial_info,
#                 additional_info=additional_info
#             )
            
#             # Redirect after successful submission
#             return redirect(self.success_url)
#         else:
#             # If any form is invalid, re-render the form with errors
#             context = {
#                 'personal_info_form': personal_info_form,
#                 'parent_info_form': parent_info_form,
#                 'academic_info_form': academic_info_form,
#                 'financial_info_form': financial_info_form,
#                 'additional_info_form': additional_info_form,
#             }
#             return render(request, self.template_name, context)
# '''