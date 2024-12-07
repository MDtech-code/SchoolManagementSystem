
from django.contrib import admin
from .models import FeeStructure, VoucherGenerationRule, StudentFeeVoucher, StudentFee, SecurityFee
from app.student.models import Student
from django.conf import settings
from django.core.mail import send_mail
from app.account.models import Role
@admin.register(FeeStructure)
class FeeStructureAdmin(admin.ModelAdmin):
    list_display = ('category', 'class_s', 'child_status', 'admission_type', 'total')
    search_fields = ('category__name', 'class_s__name', 'child_status', 'admission_type')
    list_filter = ('category', 'class_s', 'child_status', 'admission_type')
    ordering = ('category', 'class_s')

@admin.register(VoucherGenerationRule)
class VoucherGenerationRuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'issue_date', 'due_date', 'late_payment_fine')
    search_fields = ('name',)
    list_filter = ('active', 'issue_date', 'due_date')
    date_hierarchy = 'issue_date'
    ordering = ('-issue_date',)

@admin.register(StudentFeeVoucher)
class StudentFeeVoucherAdmin(admin.ModelAdmin):
    list_display = ('voucher_number', 'student', 'issue_date', 'due_date', 'total_fee', 'voucher_status')
    search_fields = ('voucher_number', 'student__student_name', 'student__father_name')
    list_filter = ('issue_date', 'due_date', 'is_paid', 'partial_paid')
    #list_editable = ('is_paid', 'amount_paid', 'date_paid')
    date_hierarchy = 'issue_date'
    ordering = ('-issue_date',)

    fieldsets = (
        (None, {
            'fields': ('voucher_number', 'student', 'class_section', 'issue_date', 'due_date')
        }),
        ('Fee Details', {
            'fields': ('tuition_fee', 'dev_fund', 'misc_fee', 'admission_fee', 'security_fee', 'prospectus_fee', 'arrears', 'advance', 'late_payment_fine', 'extra_charges', 'extra_charges_note', 'total_fee', 'total_fee_after_due_date')
        }),
        ('Arrears Details', {
            'fields': ('arrears_tuition_fee', 'arrears_development_fund', 'arrears_misc', 'arrears_fine', 'arrears_others')
        }),
        ('Payment Status', {
            'fields': ('is_paid', 'partial_paid', 'amount_paid', 'date_paid')
        }),
        ('Voucher Type', {
            'fields': ('is_security_voucher', 'is_admission_voucher', 'is_extras_voucher', 'voucher_type', 'is_advance_voucher', 'total_months_advance', 'advance_start_month', 'advance_end_month')
        }),
        ('Additional Information', {
            'fields': ('admission', 'previous_voucher')
        }),
    )
    def save_model(self, request, obj, form, change):
     super().save_model(request, obj, form, change)
     if obj.is_paid and obj.student:  # Check if is_paid is True and student object EXISTS
        student = obj.student  # Get the existing student object
        student.is_verified = True
        student.student_status = 'enrolled'  # Set the student status
        student.save()  # This will trigger roll_no generation in Student.save()
        # Update role to 'student' if available, or create it if it does not exist
        student_role, created = Role.objects.get_or_create(name='student')
        obj.role = student_role  # Assign the student role
        obj.save()  # Save to apply the role update

        # ... (your existing code to send confirmation email) ...
        # if obj.is_paid and  obj.student:
        #         student=obj.status='enrolled',
        #         student = obj.admission.student
        #         student.is_verified = True
        #         obj.student = student  # Link the voucher to the student
        #         obj.save()
        # Send confirmation email
        #send_mail(
        #        'Enrollment Confirmed!',
        #        f'Dear {student.admission.full_name},\n\nYour payment has been received, and your enrollment at [School Name] is confirmed.\n\n'
        #        f'You can now log in to the student dashboard using your roll number ({student.roll_no}) and the password you set during registration.\n\n'
        #        'Thank you,\n[School Name]',
        #        settings.EMAIL_HOST_USER,
        #        [student.admission.email],
        #        fail_silently=False,
        #)

@admin.register(StudentFee)
class StudentFeeAdmin(admin.ModelAdmin):
    list_display = ('voucher', 'amount_paid', 'date_submitted', 'paid_full', 'paid_full_after_due_date')
    search_fields = ('voucher__voucher_number', 'created_by__username')
    list_filter = ('date_submitted', 'paid_full', 'paid_full_after_due_date')
    date_hierarchy = 'date_submitted'
    ordering = ('-date_submitted',)

@admin.register(SecurityFee)
class SecurityFeeAdmin(admin.ModelAdmin):
    list_display = ('student', 'amount_paid', 'date_submitted', 'is_refunded', 'refund_date')
    search_fields = ('student__student_name', 'created_by__username')
    list_filter = ('date_submitted', 'is_refunded', 'refund_date')
    date_hierarchy = 'date_submitted'
    ordering = ('-date_submitted',)
