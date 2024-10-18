from django.contrib import admin
from .models import FeeStructure, VoucherGenerationRule, StudentFeeVoucher, StudentFee, SecurityFee

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
            'fields': ('admission', 'form_b_no', 'previous_voucher')
        }),
    )

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
