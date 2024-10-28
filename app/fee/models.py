
from django.db import models
from app.common.models import TimeStampedModel,Category
from app.academic.models import Class
from django.utils import timezone
from django.utils.html import format_html
from app.admission.models import Admission
from django.contrib.auth.models import User
from app.student.models import Student
from app.finance.models import Bank
from app.account.models import CustomUser



class FeeStructure(TimeStampedModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    class_s = models.ForeignKey(Class, on_delete=models.CASCADE, verbose_name="Class" ,null=True)
    child_status = models.CharField(max_length=64)#choices=CHILD_CHOICES
    admission_type = models.CharField(max_length=64 )#choices=ADMISSION_TYPE_CHOICES
    tuition_fee = models.PositiveIntegerField(default=0)
    development_fund = models.PositiveIntegerField(default=0)
    misc = models.PositiveIntegerField(default=0)
    admission = models.PositiveIntegerField(default=0)
    security = models.PositiveIntegerField(default=0)
    building = models.PositiveIntegerField(default=0)
    id_card_fee = models.PositiveIntegerField(default=0)
    examination = models.PositiveIntegerField(default=0)
    fine = models.PositiveIntegerField(default=0)
    prospectus = models.PositiveIntegerField(default=0)
    trip = models.PositiveIntegerField(default=0)
    others_note = models.CharField(max_length=64, null=True, blank=True)
    others = models.PositiveIntegerField(default=0)
    total = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.total} | {self.category.name} - {self.child_status} - {self.admission_type} - {self.class_s}"
    

class VoucherGenerationRule(TimeStampedModel):
    
    active = models.BooleanField()
    apply_arrears = models.BooleanField()
    created = models.DateTimeField()
    due_date = models.DateField()
    extra_charges = models.PositiveIntegerField()
    extra_charges_note = models.CharField(max_length=255)
    issue_date = models.DateField()
    late_payment_fine = models.PositiveIntegerField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

def get_due_date():
    return timezone.now().date() + timezone.timedelta(days=10)
class StudentFeeVoucher(TimeStampedModel):
    voucher_number = models.CharField(max_length=12)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    class_section = models.CharField(max_length=12, null=True, blank=True)
    time_generated = models.DateTimeField(auto_now_add=True)
    issue_date = models.DateField(default=timezone.now)
    tuition_fee = models.PositiveIntegerField(default=0)
    dev_fund = models.PositiveIntegerField(default=0)
    misc_fee = models.PositiveIntegerField(default=0)
    admission_fee = models.PositiveIntegerField(default=0)
    security_fee = models.PositiveIntegerField(default=0)
    prospectus_fee = models.PositiveIntegerField(default=0)
    arrears = models.PositiveIntegerField(default=0)
    advance = models.PositiveIntegerField(default=0)
    due_date = models.DateField(default=get_due_date)
    late_payment_fine = models.PositiveIntegerField(default=300)
    extra_charges = models.PositiveIntegerField(default=0)
    extra_charges_note = models.CharField(max_length=64, blank=True, null=True)
    total_fee = models.IntegerField(blank=True, null=True)
    total_fee_after_due_date = models.IntegerField(blank=True, null=True)
    fee_structure = models.ForeignKey(FeeStructure, on_delete=models.PROTECT)
    arrears_tuition_fee = models.PositiveIntegerField(default=0)
    arrears_development_fund = models.PositiveIntegerField(default=0)
    arrears_misc = models.PositiveIntegerField(default=0)
    arrears_fine = models.PositiveIntegerField(default=0)
    arrears_others = models.PositiveIntegerField(default=0)
    is_paid = models.BooleanField(default=False)
    partial_paid = models.BooleanField(default=False)
    amount_paid = models.PositiveIntegerField(default=0)
    date_paid = models.DateField(blank=True, null=True)

    is_security_voucher = models.BooleanField(default=False)
    is_admission_voucher = models.BooleanField(default=False)
    is_extras_voucher = models.BooleanField(default=False)
    voucher_type = models.CharField(max_length=64) #choices=VOUCHER_TYPE_CHOICES default=VOUCHER_TYPE_CHOICES[0][0]
    is_advance_voucher = models.BooleanField(default=False)
    total_months_advance = models.PositiveIntegerField(default=0, blank=True, null=True)
    advance_start_month = models.DateField(null=True, blank=True)
    advance_end_month = models.DateField(null=True, blank=True)

    admission = models.ForeignKey(Admission, null=True, blank=True, on_delete=models.PROTECT)
    form_b_no = models.CharField(max_length=15, null=True, blank=True)

    previous_voucher = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    def voucher_status(self):
        if self.is_paid:
            return format_html('<span style="color: green; font-weight: bold;">✓ Paid</span>')
        elif self.partial_paid:
            return format_html('<span style="color: yellow; font-weight: bold;">⚠ Partially Paid</span>')
        else:
            return format_html('<span style="color: red; font-weight: bold;">✗ Not Paid</span>')

    voucher_status.short_description = 'Status'

    def calculate_total_fee(self):
        return (
                self.admission_fee + self.prospectus_fee + self.arrears + self.extra_charges + self.total_fee) - self.advance

    @property
    def merged_tuition_fee(self):
        return self.fee_structure.tuition_fee + self.arrears_tuition_fee

    @property
    def merged_development_fund(self):
        return self.fee_structure.development_fund + self.arrears_development_fund

    @property
    def merged_misc(self):
        return self.fee_structure.misc + self.arrears_misc

    def __str__(self):
        return f'{self.voucher_number} | {self.total_fee} | {self.student.student_name} | {self.student.father_name} | {self.student.student_section}'

    class Meta:
        ordering = ['-issue_date']




class StudentFee(TimeStampedModel):
    
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE,null=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True)
    voucher = models.ForeignKey(StudentFeeVoucher, on_delete=models.CASCADE,null=True)
    amount_paid = models.PositiveIntegerField()
    date_submitted = models.DateField()
    paid_full = models.BooleanField()
    paid_full_after_due_date = models.BooleanField()
    paid_full_after_due_date_waive_fine = models.BooleanField()
    paid_full_after_due_date_without_fine = models.BooleanField()

    def __str__(self):
        return f"StudentFee {self.id} - Amount Paid: {self.amount_paid}"
    

class SecurityFee(TimeStampedModel):
    
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE,null=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE,null=True)
    student_fee = models.ForeignKey(StudentFee, on_delete=models.CASCADE,null=True)
    amount_paid = models.PositiveIntegerField()
    created = models.DateTimeField()
    date_submitted = models.DateField()
    is_refunded = models.BooleanField()
    paid_to = models.CharField(max_length=255)
    refund_date = models.DateField()

    def __str__(self):
        return f"SecurityFee {self.id} - Amount Paid: {self.amount_paid}"
