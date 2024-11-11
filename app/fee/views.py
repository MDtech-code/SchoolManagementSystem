from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import StudentFeeVoucher
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import StudentFeeVoucher,FeeStructure
from app.admission.models import Admission
from app.student.models import Student
from django.conf import settings
import uuid 
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML

@login_required
def generate_voucher(request, admission_id):
    admission = get_object_or_404(Admission, id=admission_id)


    

    # Check if a voucher already exists
    existing_voucher = StudentFeeVoucher.objects.filter(admission=admission).first()
    if existing_voucher:
        messages.info(request, 'A voucher has already been generated for this admission.')
        return redirect('applicant_dashboard')

    # Get the FeeStructure
    fee_structure = FeeStructure.objects.get(  
        class_s=admission.admission_class,
        category=admission.category,
        # ... add any other filters based on your FeeStructure model ...
    )
    # Calculate total fee (replace with your actual calculation logic)
    total_fee = fee_structure.tuition_fee + fee_structure.admission + fee_structure.security  
    # Generate voucher (replace with your actual voucher generation logic)
    voucher = StudentFeeVoucher.objects.create(
        admission=admission,
        voucher_number=uuid.uuid4(),  # Generate a unique voucher number
        student=Student.objects.get(admission=admission),
        fee_structure=fee_structure,
        tuition_fee=fee_structure.tuition_fee,  # Set tuition_fee from FeeStructure
        dev_fund=fee_structure.development_fund,  # Set dev_fund from FeeStructure
        misc_fee=fee_structure.misc,  # Set misc_fee from FeeStructure
        admission_fee=fee_structure.admission,  # Set admission_fee from FeeStructure
        security_fee=fee_structure.security,  # Set security_fee from FeeStructure
        prospectus_fee=fee_structure.prospectus,  # Set prospectus_fee from FeeStructure
        # ... other required fields for the voucher, set to default values or calculated based on FeeStructure ...
        total_fee=fee_structure.total,  # Set total_fee from FeeStructure
    )

    admission.is_voucher_generated = True
    admission.save()

    # Send email notification
    send_mail(
        'Voucher Generated',
        f'Dear {admission.full_name},\n\nYour fee voucher has been generated. '
        f'Please visit the applicant dashboard to view and download your voucher.\n\n'
        f'Voucher Number: {voucher.voucher_number}\n\n'
        f'Thank you,\n[army public school]',
        settings.EMAIL_HOST_USER,
        [admission.email],
        fail_silently=False,
    )

    messages.success(request, f'Voucher generated successfully! Voucher number: {voucher.voucher_number}')
    return redirect('applicant_dashboard')


@login_required
def view_voucher(request, admission_id):
    admission = get_object_or_404(Admission, id=admission_id)
    voucher = get_object_or_404(StudentFeeVoucher, admission=admission)
    context = {'voucher': voucher}
    return render(request, 'fee/voucher.html', context)








@login_required
def download_voucher(request, admission_id):
    admission = get_object_or_404(Admission, id=admission_id)
    voucher = get_object_or_404(StudentFeeVoucher, admission=admission)

    # Generate PDF from the voucher template
    template_path = 'fee/voucher.html'
    context = {'voucher': voucher}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename="voucher_{voucher.voucher_number}.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    HTML(string=html).write_pdf(response)

    return response