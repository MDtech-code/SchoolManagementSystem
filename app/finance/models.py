from django.db import models
from app.common.models import TimeStampedModel


class Bank(TimeStampedModel):
    """
    !Model representing bank details, including account information and contact details.
    """
    bank_account_no = models.CharField(
        max_length=255,
        unique=True,  # Ensure bank account number is unique
        verbose_name="Bank Account Number",
        help_text="Unique account number for the bank."
    )
    bank_address = models.CharField(
        max_length=255,
        verbose_name="Bank Address",
        help_text="Physical address of the bank."
    )
    bank_code = models.CharField(
        max_length=255,
        verbose_name="Bank Code",
        help_text="The unique code assigned to the bank."
    )
    bank_contact = models.CharField(  # Changed to CharField for flexibility
        max_length=20,
        verbose_name="Bank Contact Number",
        help_text="Contact number for the bank."
    )
    bank_for_security = models.BooleanField(
        default=False,
        verbose_name="Security Flag",
        help_text="Indicates if the bank is for security purposes."
    )
    bank_manager = models.CharField(
        max_length=255,
        verbose_name="Bank Manager",
        help_text="Name of the bank manager."
    )
    bank_name = models.CharField(
        max_length=255,
        verbose_name="Bank Name",
        help_text="Name of the bank."
    )
    show_on_voucher = models.BooleanField(
        default=False,
        verbose_name="Show on Voucher",
        help_text="Indicates if the bank details should be shown on vouchers."
    )

    class Meta:
        verbose_name = "Bank"
        verbose_name_plural = "Banks"
        indexes = [
            models.Index(fields=['bank_name'], name='bank_name_idx')  # Index for faster lookups on bank name
        ]

    def __str__(self):
        return self.bank_name


class Expense(TimeStampedModel):
    """
    !Model representing an expense entry, including details about the amount and description.
    """
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Expense Amount",
        help_text="Amount of the expense."
    )
    date = models.DateField(
        verbose_name="Expense Date",
        help_text="Date of the expense."
    )
    description = models.TextField(
        verbose_name="Description",
        help_text="Detailed description of the expense."
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Expense Title",
        help_text="Title of the expense."
    )

    class Meta:
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"
        indexes = [
            models.Index(fields=['date'], name='expense_date_idx')  # Index for faster lookups on date
        ]

    def __str__(self):
        return self.title


class Loan(TimeStampedModel):
    """
    !Model representing a loan taken by an employee, tracking amounts and installments.
    """
    employee = models.ForeignKey(
        'employee.Employee',
        on_delete=models.CASCADE,
        verbose_name="Employee",
        help_text="The employee who has taken the loan."
    )
    loan_amount = models.FloatField(
        verbose_name="Loan Amount",
        help_text="Total amount of the loan taken."
    )
    remaining_amount = models.FloatField(
        verbose_name="Remaining Amount",
        help_text="Amount still outstanding on the loan."
    )
    total_installments = models.PositiveIntegerField(
        verbose_name="Total Installments",
        help_text="Total number of installments for repayment."
    )

    class Meta:
        verbose_name = "Loan"
        verbose_name_plural = "Loans"
        indexes = [
            models.Index(fields=['employee'], name='loan_employee_idx')  # Index for faster lookups on employee
        ]

    def __str__(self):
        return f"Loan for {self.employee.employee_name}"

class InstallmentPaid(TimeStampedModel):
    """
    !Model representing an installment payment for a loan.
    """
    loan = models.ForeignKey(
        'Loan',
        on_delete=models.CASCADE,
        verbose_name="Loan",
        help_text="The loan for which the installment is paid."
    )
    amount_paid = models.FloatField(
        verbose_name="Amount Paid",
        help_text="Amount of the installment that has been paid."
    )
    date_paid = models.DateField(
        verbose_name="Date Paid",
        help_text="The date when the installment was paid."
    )

    class Meta:
        verbose_name = "Installment Paid"
        verbose_name_plural = "Installments Paid"
        indexes = [
            models.Index(fields=['loan'], name='installment_loan_idx'),  # Index for faster lookups on loan
            models.Index(fields=['date_paid'], name='installment_date_idx')  # Index for faster lookups on date
        ]

    def __str__(self):
        return f"Installment Paid for {self.loan.employee.employee_name}"


class IncomeTaxSession(TimeStampedModel):
    """
    !Model representing an income tax session, defined by starting and ending years.
    """
    starting_year = models.DateField(
        verbose_name="Starting Year",
        help_text="The year when the income tax session starts."
    )
    ending_year = models.DateField(
        verbose_name="Ending Year",
        help_text="The year when the income tax session ends."
    )

    class Meta:
        verbose_name = "Income Tax Session"
        verbose_name_plural = "Income Tax Sessions"
        indexes = [
            models.Index(fields=['starting_year'], name='income_tax_start_idx'),  # Index for faster lookups on starting year
        ]

    def __str__(self):
        return f"Income Tax Session {self.starting_year} - {self.ending_year}"


class IncomeTaxRates(TimeStampedModel):
    """
    !Model representing income tax rates for a specific session.
    """
    session = models.ForeignKey(
        'IncomeTaxSession',
        on_delete=models.CASCADE,
        verbose_name="Income Tax Session",
        help_text="The session to which these tax rates apply."
    )
    initial_taxable_income = models.PositiveIntegerField(
        verbose_name="Initial Taxable Income",
        help_text="The starting amount of taxable income."
    )
    to_taxable_income = models.PositiveIntegerField(
        verbose_name="To Taxable Income",
        help_text="The ending amount of taxable income."
    )
    percentage = models.FloatField(
        verbose_name="Tax Percentage",
        help_text="The percentage of tax applied within this income bracket."
    )

    class Meta:
        verbose_name = "Income Tax Rate"
        verbose_name_plural = "Income Tax Rates"
        unique_together = (('session', 'initial_taxable_income', 'to_taxable_income'),)  # Ensure unique income brackets
        indexes = [
            models.Index(fields=['session'], name='income_tax_session_idx'),  # Index for faster lookups on session
        ]

    def __str__(self):
        return f"Tax Rate for {self.session}"


class CPFund(TimeStampedModel):
    """
    !Model representing a CP fund associated with an employee.
    """
    created_by = models.ForeignKey(
        'account.CustomUser',
        on_delete=models.CASCADE,
        related_name="created_funds",
        null=True,
        verbose_name="Created By",
        help_text="User who created this CP Fund."
    )
    employee = models.OneToOneField(
        'account.CustomUser',
        on_delete=models.CASCADE,
        related_name="cpfund",
        null=True,
        verbose_name="Employee",
        help_text="The employee associated with this CP Fund."
    )
    deposited_cp_fund = models.PositiveIntegerField(
        verbose_name="Deposited CP Fund",
        help_text="Amount deposited into the CP Fund."
    )
    last_date_submitted = models.DateField(
        verbose_name="Last Date Submitted",
        help_text="The last date when the CP Fund was submitted."
    )

    class Meta:
        verbose_name = "CP Fund"
        verbose_name_plural = "CP Funds"
        indexes = [
            models.Index(fields=['employee'], name='cpf_employee_idx'),  # Index for faster lookups on employee
        ]

    def __str__(self):
        return f"CPFund for {self.employee.username} - {self.deposited_cp_fund}"


class EOBIPaid(TimeStampedModel):
    """
    !Model representing EOBI payments made for an employee.
    """
    created_by = models.ForeignKey(
        'account.CustomUser',
        on_delete=models.CASCADE,
        related_name="eobi_created_by",
        null=True,
        verbose_name="Created By",
        help_text="User who created this EOBI payment entry."
    )
    employee = models.ForeignKey(
        'account.CustomUser',
        on_delete=models.CASCADE,
        related_name="eobi_employee",
        null=True,
        verbose_name="Employee",
        help_text="The employee for whom the EOBI payment is made."
    )
    eobi_date_of_joining = models.DateField(
        verbose_name="Date of Joining",
        help_text="The date when the employee joined."
    )
    month = models.DateField(
        verbose_name="Month",
        help_text="The month for which the EOBI payment is made."
    )
    total_deposit = models.FloatField(
        verbose_name="Total Deposit",
        help_text="Total amount deposited for EOBI."
    )

    class Meta:
        verbose_name = "EOBI Payment"
        verbose_name_plural = "EOBI Payments"
        indexes = [
            models.Index(fields=['employee'], name='eobi_employee_idx'),  # Index for faster lookups on employee
            models.Index(fields=['month'], name='eobi_month_idx'),  # Index for faster lookups on month
        ]

    def __str__(self):
        return f"EOBI Payment for {self.employee.username} - {self.total_deposit}"


class CPFundDeposits(TimeStampedModel):
    """
    !Model representing deposits made to a CP fund.
    """
    cp_fund = models.ForeignKey(
        'CPFund',
        on_delete=models.CASCADE,
        related_name="deposits",
        verbose_name="CP Fund",
        help_text="The CP Fund to which the deposit is made."
    )
    created_by = models.ForeignKey(
        'account.CustomUser',
        on_delete=models.CASCADE,
        related_name="cpfund_deposits_created_by",
        null=True,
        verbose_name="Created By",
        help_text="User who created this deposit entry."
    )
    amount = models.PositiveIntegerField(
        verbose_name="Amount",
        help_text="The amount deposited to the CP fund."
    )
    date_paid = models.DateField(
        verbose_name="Date Paid",
        help_text="The date when the deposit was made."
    )
    note = models.CharField(
        max_length=255,
        verbose_name="Note",
        help_text="Any additional notes regarding the deposit."
    )

    class Meta:
        verbose_name = "CP Fund Deposit"
        verbose_name_plural = "CP Fund Deposits"
        indexes = [
            models.Index(fields=['cp_fund'], name='cpf_deposit_fund_idx'),  # Index for faster lookups on cp_fund
            models.Index(fields=['date_paid'], name='cpf_deposit_date_idx'),  # Index for faster lookups on date_paid
        ]

    def __str__(self):
        return f"CPFund Deposit of {self.amount} by {self.created_by.username} on {self.date_paid}"


class EmployeeArrears(TimeStampedModel):
    """
    !Model representing arrears for an employee.
    """
    employee = models.OneToOneField(
        'account.CustomUser',
        on_delete=models.CASCADE,
        related_name="employee_arrears",
        null=True,
        verbose_name="Employee",
        help_text="The employee associated with these arrears."
    )
    arrears_amount = models.IntegerField(
        verbose_name="Arrears Amount",
        help_text="Total amount of arrears for the employee."
    )
    arrears_note = models.CharField(
        max_length=255,
        verbose_name="Arrears Note",
        help_text="Notes regarding the arrears."
    )

    class Meta:
        verbose_name = "Employee Arrears"
        verbose_name_plural = "Employee Arrears"

    def __str__(self):
        return f"Arrears for {self.employee.username} - {self.arrears_amount}"


class Security(TimeStampedModel):
    """
    !Model representing security deposits made for an employee.
    """
    created_by = models.ForeignKey(
        'employee.Employee',
        on_delete=models.CASCADE,
        related_name='created_security',
        verbose_name="Created By",
        help_text="Employee who created this security entry."
    )
    employee = models.OneToOneField(
        'employee.Employee',
        on_delete=models.CASCADE,
        related_name='employee_security',
        verbose_name="Employee",
        help_text="The employee associated with this security deposit."
    )
    deposited_security = models.PositiveIntegerField(
        verbose_name="Deposited Security",
        help_text="Amount deposited as security."
    )
    last_date_submitted = models.DateField(
        verbose_name="Last Date Submitted",
        help_text="The last date when the security deposit was made."
    )
    total_security = models.PositiveIntegerField(
        verbose_name="Total Security",
        help_text="Total security amount deposited."
    )

    class Meta:
        verbose_name = "Security"
        verbose_name_plural = "Securities"
        indexes = [
            models.Index(fields=['employee'], name='security_employee_idx'),  # Index for faster lookups on employee
        ]

    def __str__(self):
        return f"Security for {self.employee}"
    
class SecurityDeposits(TimeStampedModel):
    """
    !Model representing security deposits made for a security.
    """
    created_by = models.ForeignKey(
        'employee.Employee',
        on_delete=models.CASCADE,
        related_name='created_security_deposits',
        verbose_name="Created By",
        help_text="Employee who created this security deposit entry."
    )
    security = models.ForeignKey(
        'Security',
        on_delete=models.CASCADE,
        related_name='security_deposits',
        verbose_name="Security",
        help_text="The security associated with this deposit."
    )
    amount = models.PositiveIntegerField(
        verbose_name="Deposit Amount",
        help_text="The amount deposited as security."
    )
    date_paid = models.DateField(
        verbose_name="Date Paid",
        help_text="The date when the security deposit was made."
    )
    note = models.CharField(
        max_length=255,
        verbose_name="Note",
        help_text="Any additional notes regarding the security deposit."
    )

    class Meta:
        verbose_name = "Security Deposit"
        verbose_name_plural = "Security Deposits"
        indexes = [
            models.Index(fields=['security'], name='security_deposit_security_idx'),  # Index for faster lookups on security
            models.Index(fields=['date_paid'], name='security_deposit_date_idx'),  # Index for faster lookups on date_paid
        ]

    def __str__(self):
        return f"Security Deposit for {self.security} by {self.created_by}"


class OtherDeposits(TimeStampedModel):
    """
    !Model representing other deposits made to a bank.
    """
    bank = models.ForeignKey(
        'Bank',
        on_delete=models.CASCADE,
        related_name='other_deposits',
        verbose_name="Bank",
        help_text="The bank where the deposit is made."
    )
    amount = models.PositiveIntegerField(
        verbose_name="Deposit Amount",
        help_text="The amount deposited to the bank."
    )
    date = models.DateField(
        verbose_name="Deposit Date",
        help_text="The date when the deposit was made."
    )
    remarks = models.CharField(
        max_length=255,
        verbose_name="Remarks",
        help_text="Any additional remarks regarding the deposit."
    )

    class Meta:
        verbose_name = "Other Deposit"
        verbose_name_plural = "Other Deposits"
        indexes = [
            models.Index(fields=['bank'], name='other_deposit_bank_idx'),  # Index for faster lookups on bank
            models.Index(fields=['date'], name='other_deposit_date_idx'),  # Index for faster lookups on date
        ]

    def __str__(self):
        return f"Other Deposit to {self.bank} on {self.date}"


class MonthClosing(TimeStampedModel):
    """
    !Model representing the monthly closing for a bank.
    """
    bank = models.ForeignKey(
        'Bank',
        on_delete=models.CASCADE,
        related_name='month_closings',
        verbose_name="Bank",
        help_text="The bank associated with this month closing."
    )
    month = models.DateField(
        verbose_name="Closing Month",
        help_text="The month for which the closing is calculated."
    )
    profit_by_bank = models.PositiveIntegerField(
        verbose_name="Profit",
        help_text="The profit calculated for this month closing."
    )

    class Meta:
        verbose_name = "Month Closing"
        verbose_name_plural = "Month Closings"
        unique_together = ('bank', 'month')  # Ensure unique closing for each month per bank
        indexes = [
            models.Index(fields=['bank'], name='month_closing_bank_idx'),  # Index for faster lookups on bank
            models.Index(fields=['month'], name='month_closing_month_idx'),  # Index for faster lookups on month
        ]

    def __str__(self):
        return f"Month Closing for {self.bank} - {self.month}"