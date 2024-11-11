from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Admission
from .forms import AdmissionForm
from app.account.decorators import role_required

@login_required
def apply_for_admission(request):
    if request.method == 'POST':
        form = AdmissionForm(request.POST)
        if form.is_valid():
            admission = form.save(commit=False)
            admission.applicant = request.user
            admission.save()  # This will also trigger the admission_no generation in the model's save() method
            messages.success(request, 'Admission application submitted successfully!')
            return redirect('applicant_dashboard')  # Redirect to a success page
    else:
        form = AdmissionForm()

    context = {'form': form}
    return render(request, 'admission/admission_form.html', context)