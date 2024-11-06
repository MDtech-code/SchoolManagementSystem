# from django.db import models
# from app.common.models import TimeStampedModel
# from app.employee.models import Employee
# from django.contrib.auth.models import User
# from app.account.models import CustomUser
# from django.conf import settings
# from django.db.models import UniqueConstraint

# #! Represents the pay structure for different employee designations
# class PayStructure(TimeStampedModel):
#     employee_designation = models.ForeignKey(
#         'employee.EmployeeDesignation', 
#         on_delete=models.CASCADE, 
#         related_name="pay_structures",  #! This will be used as a reference to access related pay structures from other models.
#         verbose_name="Employee Designation",#!Verbose Names are used for better readbality in the forms and Admin interface.
#         help_text="Select the designation related to this pay structure.",  #! This text provides guidance on what designation to select for the corresponding pay structure.
#     )
#     annual_increment = models.IntegerField(
#         verbose_name="Annual Increment",
#         help_text="Enter the annual increment amount."
#     )
#     basic_pay = models.IntegerField(
#         verbose_name="Basic Pay",
#         help_text="Enter the basic pay amount."
#     )
#     conveyance_allowance = models.IntegerField(
#         verbose_name="Conveyance Allowance",
#         help_text="Enter the conveyance allowance amount."
#     )
#     hra = models.IntegerField(
#         verbose_name="House Rent Allowance (HRA)",
#         help_text="Enter the house rent allowance amount."
#     )
#     medical_allowance = models.IntegerField(
#         verbose_name="Medical Allowance",
#         help_text="Enter the medical allowance amount."
#     )

#     class Meta:
#         verbose_name = "Pay Structure"
#         verbose_name_plural = "Pay Structures"
#         ordering = ["-created_at"]
#         constraints = [
#             UniqueConstraint(fields=['employee_designation'], name='unique_pay_structure_per_designation')
#         ]
#         indexes = [
#             models.Index(fields=['employee_designation']),
#             models.Index(fields=['basic_pay']),
#         ]

#     def __str__(self):
#         return f"{self.employee_designation.name} - Pay Structure"
    
# #! Represents the pay structure assigned to an employee, including various allowances
# class EmployeePayStructure(TimeStampedModel):
#     employee = models.ForeignKey(
#         Employee, 
#         on_delete=models.CASCADE, 
#         related_name="pay_structures", 
#         verbose_name="Employee"
#     )
#     employee_pay_structure = models.ForeignKey(
#         'PayStructure', 
#         on_delete=models.CASCADE, 
#         related_name="employee_pay_structures",
#         verbose_name="Pay Structure"
#     )
#     inc_aug_15_allowance = models.PositiveIntegerField(verbose_name="Inc. Aug '15 Allowance")
#     inc_aug_17_svc_allowance = models.PositiveIntegerField(verbose_name="Inc. Aug '17 Service Allowance")
#     inc_sep_21_svc_allowance = models.PositiveIntegerField(verbose_name="Inc. Sep '21 Service Allowance")
#     mphil_phd_allowance = models.PositiveIntegerField(verbose_name="MPhil/PhD Allowance")
#     spec_head_hunting_allowance = models.PositiveIntegerField(verbose_name="Special Head-Hunting Allowance")
#     svc_allowance = models.PositiveIntegerField(verbose_name="Service Allowance")

#     class Meta:
#         verbose_name = "Employee Pay Structure"
#         verbose_name_plural = "Employee Pay Structures"
#         ordering = ["-created_at"]
#         constraints = [
#             UniqueConstraint(fields=['employee', 'employee_pay_structure'], name='unique_employee_pay_structure')
#         ]
#         indexes = [
#             models.Index(fields=['employee']),
#             models.Index(fields=['employee_pay_structure']),
#         ]

#     def __str__(self):
#         return f"{self.employee.employee_name} - Pay Structure"

# #! Represents the payroll details for each employee, including various allowances and deductions
# class Payroll(TimeStampedModel):
#     employee = models.ForeignKey(
#         CustomUser, 
#         on_delete=models.CASCADE, 
#         related_name="payrolls", 
#         verbose_name="Employee", 
#         null=True
#     )
#     employee_pay_structure = models.ForeignKey(
#         EmployeePayStructure, 
#         on_delete=models.CASCADE, 
#         related_name="payrolls", 
#         verbose_name="Pay Structure"
#     )

#     annual_increments = models.FloatField(verbose_name="Annual Increments")
#     arrears = models.PositiveIntegerField(verbose_name="Arrears")
#     conveyance_allowance = models.PositiveIntegerField(verbose_name="Conveyance Allowance")
#     cp_fund = models.PositiveIntegerField(verbose_name="CP Fund")
#     date_issued = models.DateField(verbose_name="Date Issued")
#     education_allowance = models.PositiveIntegerField(verbose_name="Education Allowance")
#     employee_oldage_benefit_inst = models.PositiveIntegerField(verbose_name="Old-Age Benefit")
#     eobi = models.PositiveIntegerField(verbose_name="EOBI")
#     house_rent_allowance = models.PositiveIntegerField(verbose_name="House Rent Allowance")
#     inc_aug_15_allowance = models.PositiveIntegerField(verbose_name="Aug '15 Increment Allowance")
#     inc_aug_17_svc_allowance = models.PositiveIntegerField(verbose_name="Aug '17 Service Allowance")
#     inc_sep_21_svc_allowance = models.PositiveIntegerField(verbose_name="Sep '21 Service Allowance")
#     income_tax = models.PositiveIntegerField(verbose_name="Income Tax")
#     increments = models.FloatField(verbose_name="Increments")
#     is_paid = models.BooleanField(default=False, verbose_name="Is Paid")
#     loan_installment = models.FloatField(verbose_name="Loan Installment")
#     lowp = models.PositiveIntegerField(verbose_name="Loss of Pay Deduction")
#     medical_allowance = models.PositiveIntegerField(verbose_name="Medical Allowance")
#     mphil_phd_allowance = models.PositiveIntegerField(verbose_name="MPhil/PhD Allowance")
#     pay_roll_no = models.CharField(max_length=255, verbose_name="Payroll Number")
#     payment_method = models.CharField(max_length=50, verbose_name="Payment Method")
#     security_deposit = models.PositiveIntegerField(verbose_name="Security Deposit")
#     spec_head_huntimg_allowance = models.PositiveIntegerField(verbose_name="Special Head-Hunting Allowance")
#     svc_allowance = models.PositiveIntegerField(verbose_name="Service Allowance")
#     time_generated = models.DateTimeField(auto_now_add=True, verbose_name="Time Generated")
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total Amount")

#     class Meta:
#         verbose_name = "Payroll"
#         verbose_name_plural = "Payrolls"
#         ordering = ["-date_issued"]
#         constraints = [
#             UniqueConstraint(fields=['employee', 'date_issued'], name='unique_payroll_per_employee_and_date'),
#             UniqueConstraint(fields=['pay_roll_no'], name='unique_payroll_number')
#         ]
#         indexes = [
#             models.Index(fields=['employee']),
#             models.Index(fields=['date_issued']),
#             models.Index(fields=['employee_pay_structure']),
#             models.Index(fields=['pay_roll_no']),
#         ]

#     def __str__(self):
#         return f"Payroll for {self.employee.username} - {self.total_amount}"

# #! Represents the annual increments awarded to employees
# class EmployeeAnnualIncrement(TimeStampedModel):
#     employee_structure = models.ForeignKey(
#         'EmployeePayStructure', 
#         on_delete=models.CASCADE, 
#         related_name="annual_increments",
#         verbose_name="Employee Pay Structure"
#     )
#     annual_inc_no = models.PositiveIntegerField(verbose_name="Annual Increment Number")
#     date_awarded = models.DateField(verbose_name="Date Awarded")
#     rate_of_annual_inc = models.CharField(max_length=100, verbose_name="Rate of Increment")
#     total_annual_inc = models.PositiveIntegerField(verbose_name="Total Annual Increment")

#     class Meta:
#         verbose_name = "Employee Annual Increment"
#         verbose_name_plural = "Employee Annual Increments"
#         ordering = ["-date_awarded"]
#         constraints = [
#             UniqueConstraint(fields=['employee_structure', 'annual_inc_no'], name='unique_increment_per_employee_structure_and_number')
#         ]

#     def __str__(self):
#         return f"Annual Increment #!{self.annual_inc_no} for {self.employee_structure} - {self.total_annual_inc}"

# #! Represents orders for increments to be processed
# class IncrementOrder(TimeStampedModel):
#     created = models.DateTimeField(auto_now_add=True, verbose_name="Order Creation Date")
#     note = models.CharField(max_length=255, verbose_name="Order Note")
#     percentage_increment = models.FloatField(verbose_name="Percentage Increment")

#     class Meta:
#         verbose_name = "Increment Order"
#         verbose_name_plural = "Increment Orders"
#         ordering = ["-created"]

#     def __str__(self):
#         return f"Increment Order - {self.percentage_increment}%"

# #! Represents increments awarded to employees based on orders
# class Increment(TimeStampedModel):
#     order = models.ForeignKey(
#         IncrementOrder, on_delete=models.CASCADE, related_name="increments",
#         verbose_name="Related Increment Order"
#     )
#     pay_structure = models.ForeignKey(
#         'EmployeePayStructure', on_delete=models.CASCADE, related_name="increments",
#         verbose_name="Employee Pay Structure"
#     )
#     amount = models.PositiveIntegerField(verbose_name="Increment Amount")
#     created = models.DateTimeField(auto_now_add=True, verbose_name="Increment Date")

#     class Meta:
#         verbose_name = "Employee Increment"
#         verbose_name_plural = "Employee Increments"
#         ordering = ["-created"]
#         constraints = [
#             UniqueConstraint(fields=['order', 'pay_structure'], name='unique_increment_per_order_and_pay_structure')
#         ]

#     def __str__(self):
#         return f"Increment for {self.pay_structure} - Amount: {self.amount}"

# #! Represents different types of leave available to employees
# class LeaveType(TimeStampedModel):
#     name = models.CharField(max_length=100, verbose_name="Leave Type Name")
#     days_paid = models.PositiveIntegerField(verbose_name="Paid Days Allowed")
#     department = models.CharField(max_length=100, verbose_name="Department")
#     granted_times_in_service = models.PositiveIntegerField(verbose_name="Total Times Granted")
#     granted_times_interval = models.PositiveIntegerField(verbose_name="Grant Interval (Months)")

#     class Meta:
#         verbose_name = "Leave Type"
#         verbose_name_plural = "Leave Types"
#         constraints = [
#             UniqueConstraint(fields=['name', 'department'], name='unique_leave_type_per_department')
#         ]

#     def __str__(self):
#         return self.name

# #! Represents leave applications made by employees
# class Leaves(TimeStampedModel):
#     deducted_in_payroll = models.ForeignKey(
#         Payroll,
#         on_delete=models.SET_NULL,
#         null=True,
#         related_name="leaves_deducted",
#         verbose_name="Deducted in Payroll",
#         help_text="Select the payroll record to which this leave is deducted."
#     )
#     employee = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         related_name="employee_leaves",
#         null=True,
#         verbose_name="Employee",
#         help_text="Select the employee requesting the leave."
#     )
#     leave_type = models.ForeignKey(
#         LeaveType,
#         on_delete=models.CASCADE,
#         related_name="leave_type_leaves",
#         verbose_name="Type of Leave",
#         help_text="Select the type of leave."
#     )
#     deductions = models.PositiveIntegerField(
#         verbose_name="Payroll Deduction Amount",
#         help_text="Enter the amount to be deducted from payroll for this leave."
#     )
#     executive_approval = models.BooleanField(
#         default=False,
#         verbose_name="Executive Approval",
#         help_text="Has the executive approved this leave?"
#     )
#     leave_date = models.DateField(
#         verbose_name="Leave Start Date",
#         help_text="Select the start date for the leave."
#     )
#     leave_end_date = models.DateField(
#         verbose_name="Leave End Date",
#         help_text="Select the end date for the leave."
#     )
#     note = models.TextField(
#         blank=True,
#         verbose_name="Leave Notes",
#         help_text="Add any additional notes regarding the leave."
#     )
#     principal_approval = models.BooleanField(
#         default=False,
#         verbose_name="Principal Approval",
#         help_text="Has the principal approved this leave?"
#     )
#     reason = models.TextField(
#         verbose_name="Reason for Leave",
#         help_text="Provide a reason for taking the leave."
#     )
#     request_date = models.DateField(
#         auto_now_add=True,
#         verbose_name="Request Date",
#         help_text="The date when the leave request was made."
#     )
#     secretary_approval = models.BooleanField(
#         default=False,
#         verbose_name="Secretary Approval",
#         help_text="Has the secretary approved this leave?"
#     )
#     status = models.CharField(
#         max_length=50,
#         verbose_name="Leave Status",
#         help_text="Current status of the leave request."
#     )
#     vc_approval = models.BooleanField(
#         default=False,
#         verbose_name="Vice Chancellor Approval",
#         help_text="Has the Vice Chancellor approved this leave?"
#     )

#     class Meta:
#         verbose_name = "Leave"
#         verbose_name_plural = "Leaves"
#         ordering = ["-request_date"]
#         constraints = [
#             UniqueConstraint(fields=['employee', 'leave_date'], name='unique_leave_per_employee_and_date'),
#         ]

#     def __str__(self):
#         return f"Leave for {self.employee.username if self.employee else 'Unknown Employee'} - Status: {self.status}"
    
