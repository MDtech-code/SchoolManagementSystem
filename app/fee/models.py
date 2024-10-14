'''
from django.db import models
from student.models import Student

class FeeStructure(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    tuition_fee = models.PositiveIntegerField(default=0)
    admission_fee = models.PositiveIntegerField(default=0)
    security_fee = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Fee Structure for {self.student.student_name}"

class StudentFee(models.Model):
    bank = models.CharField(max_length=50)
    created_by = models.ForeignKey(Student, on_delete=models.CASCADE)
    voucher = models.ForeignKey('StudentFeeVoucher', on_delete=models.CASCADE)
    amount_paid = models.PositiveIntegerField(default=0)
    date_submitted = models.DateField()
    paid_full = models.BooleanField(default=False)

    def __str__(self):
        return f"Student Fee - {self.created_by.student_name}"

class StudentFeeVoucher(models.Model):
    admission = models.ForeignKey('admission.Admission', on_delete=models.CASCADE)
    fee_structure = models.ForeignKey(FeeStructure, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    admission_fee = models.PositiveIntegerField(default=0)
    advance = models.PositiveIntegerField(default=0)
    due_date = models.DateField()
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Fee Voucher - {self.student.student_name}"

class SecurityFee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount_paid = models.PositiveIntegerField(default=0)
    is_refunded = models.BooleanField(default=False)

    def __str__(self):
        return f"Security Fee for {self.student.student_name}"

class VoucherGenerationRule(models.Model):
    name = models.CharField(max_length=128)
    issue_date = models.DateField()
    due_date = models.DateField()
    late_payment_fine = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Rule: {self.name}"

'''