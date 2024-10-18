from django.contrib import admin
from .models import Bank, Expense, Loan, InstallmentPaid, IncomeTaxSession, IncomeTaxRates, CPFund, EOBIPaid, CPFundDeposits, EmployeeArrears, Security, SecurityDeposits, OtherDeposits, MonthClosing

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('bank_name', 'bank_account_no', 'bank_manager', 'bank_contact', 'show_on_voucher')
    search_fields = ('bank_name', 'bank_account_no', 'bank_manager')
    list_filter = ('bank_for_security', 'show_on_voucher')
    ordering = ('bank_name',)

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'date', 'description')
    search_fields = ('title',)
    list_filter = ('date',)
    date_hierarchy = 'date'
    ordering = ('-date',)

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('employee', 'loan_amount', 'remaining_amount', 'total_installments')
    search_fields = ('employee__employee_name',)
    list_filter = ('loan_amount',)
    ordering = ('-loan_amount',)

@admin.register(InstallmentPaid)
class InstallmentPaidAdmin(admin.ModelAdmin):
    list_display = ('loan', 'amount_paid', 'date_paid')
    search_fields = ('loan__employee__employee_name',)
    list_filter = ('date_paid',)
    date_hierarchy = 'date_paid'
    ordering = ('-date_paid',)

@admin.register(IncomeTaxSession)
class IncomeTaxSessionAdmin(admin.ModelAdmin):
    list_display = ('starting_year', 'ending_year')
    search_fields = ('starting_year', 'ending_year')
    ordering = ('-starting_year',)

@admin.register(IncomeTaxRates)
class IncomeTaxRatesAdmin(admin.ModelAdmin):
    list_display = ('session', 'initial_taxable_income', 'to_taxable_income', 'percentage')
    search_fields = ('session__starting_year', 'session__ending_year')
    list_filter = ('session',)
    ordering = ('session',)

@admin.register(CPFund)
class CPFundAdmin(admin.ModelAdmin):
    list_display = ('employee', 'deposited_cp_fund', 'last_date_submitted')
    search_fields = ('employee__username',)
    list_filter = ('last_date_submitted',)
    date_hierarchy = 'last_date_submitted'
    ordering = ('-last_date_submitted',)

@admin.register(EOBIPaid)
class EOBIPaidAdmin(admin.ModelAdmin):
    list_display = ('employee', 'total_deposit', 'month', 'eobi_date_of_joining')
    search_fields = ('employee__username',)
    list_filter = ('month', 'eobi_date_of_joining')
    date_hierarchy = 'month'
    ordering = ('-month',)

@admin.register(CPFundDeposits)
class CPFundDepositsAdmin(admin.ModelAdmin):
    list_display = ('cp_fund', 'amount', 'date_paid', 'note')
    search_fields = ('cp_fund__employee__username',)
    list_filter = ('date_paid',)
    date_hierarchy = 'date_paid'
    ordering = ('-date_paid',)

@admin.register(EmployeeArrears)
class EmployeeArrearsAdmin(admin.ModelAdmin):
    list_display = ('employee', 'arrears_amount', 'arrears_note')
    search_fields = ('employee__username',)
    ordering = ('-arrears_amount',)

@admin.register(Security)
class SecurityAdmin(admin.ModelAdmin):
    list_display = ('employee', 'deposited_security', 'last_date_submitted', 'total_security')
    search_fields = ('employee__employee_name',)
    list_filter = ('last_date_submitted',)
    date_hierarchy = 'last_date_submitted'
    ordering = ('-last_date_submitted',)

@admin.register(SecurityDeposits)
class SecurityDepositsAdmin(admin.ModelAdmin):
    list_display = ('security', 'amount', 'date_paid', 'note')
    search_fields = ('security__employee__employee_name',)
    list_filter = ('date_paid',)
    date_hierarchy = 'date_paid'
    ordering = ('-date_paid',)

@admin.register(OtherDeposits)
class OtherDepositsAdmin(admin.ModelAdmin):
    list_display = ('bank', 'amount', 'date', 'remarks')
    search_fields = ('bank__bank_name',)
    list_filter = ('date',)
    date_hierarchy = 'date'
    ordering = ('-date',)

@admin.register(MonthClosing)
class MonthClosingAdmin(admin.ModelAdmin):
    list_display = ('bank', 'month', 'profit_by_bank')
    search_fields = ('bank__bank_name',)
    list_filter = ('month',)
    date_hierarchy = 'month'
    ordering = ('-month',)
