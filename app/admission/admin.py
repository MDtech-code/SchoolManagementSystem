from django.contrib import admin
from django.core.mail import send_mail
from .models import Occupation,Admission
from app.student.models import Student
from django.conf import settings
from app.fee.models import StudentFeeVoucher
admin.site.register(Occupation)


class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'admission_class', 'admission_status', 'created_at')  # Display relevant fields
    list_filter = ('admission_status', 'admission_class')  # Add filters
    search_fields = ('full_name', 'admission_no')  # Add search functionality
    readonly_fields = ('admission_no',)  # Make admission_no read-only
    actions = ['approve_application', 'reject_application']  # Add custom actions
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)  # Save the Admission userect first

        if obj.admission_status == 'approved':
            # Create Student userect
            student = Student.objects.create(
                admission=obj,
                user=obj.applicant,
                is_verified=False,
                student_status='enrolled',
            )
            
            # Send confirmation email
            send_mail(
                'Admission Confirmed!',
                f'Congratulations! Your admission to army public school has been confirmed. Your roll number is {student.roll_no}.',
                settings.EMAIL_HOST_USER,  # Replace with your email
                [obj.email],
                fail_silently=False,
            )
        elif obj.admission_status == 'rejected':
            # Send rejection email
            send_mail(
                'Admission Rejected',
                f'Dear {obj.full_name},\n\nWe regret to inform you that your admission to [School Name] has been rejected.\n\n'
                'Please contact the school for more information.\n\n'
                'Thank you,\n[School Name]',
                settings.EMAIL_HOST_USER,
                [obj.email],
                fail_silently=False,
            )
        # # Update the voucher with the student object
        # try:
        #     voucher = StudentFeeVoucher.objects.get(admission=obj)
        #     voucher.student = student
        #     voucher.save()
        # except StudentFeeVoucher.DoesNotExist:
        #     pass

        
            




admin.site.register(Admission, AdmissionAdmin)