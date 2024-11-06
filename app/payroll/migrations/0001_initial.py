# Generated by Django 4.2.16 on 2024-11-06 19:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeAnnualIncrement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('annual_inc_no', models.PositiveIntegerField(verbose_name='Annual Increment Number')),
                ('date_awarded', models.DateField(verbose_name='Date Awarded')),
                ('rate_of_annual_inc', models.CharField(max_length=100, verbose_name='Rate of Increment')),
                ('total_annual_inc', models.PositiveIntegerField(verbose_name='Total Annual Increment')),
            ],
            options={
                'verbose_name': 'Employee Annual Increment',
                'verbose_name_plural': 'Employee Annual Increments',
                'ordering': ['-date_awarded'],
            },
        ),
        migrations.CreateModel(
            name='EmployeePayStructure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('inc_aug_15_allowance', models.PositiveIntegerField(verbose_name="Inc. Aug '15 Allowance")),
                ('inc_aug_17_svc_allowance', models.PositiveIntegerField(verbose_name="Inc. Aug '17 Service Allowance")),
                ('inc_sep_21_svc_allowance', models.PositiveIntegerField(verbose_name="Inc. Sep '21 Service Allowance")),
                ('mphil_phd_allowance', models.PositiveIntegerField(verbose_name='MPhil/PhD Allowance')),
                ('spec_head_hunting_allowance', models.PositiveIntegerField(verbose_name='Special Head-Hunting Allowance')),
                ('svc_allowance', models.PositiveIntegerField(verbose_name='Service Allowance')),
            ],
            options={
                'verbose_name': 'Employee Pay Structure',
                'verbose_name_plural': 'Employee Pay Structures',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Increment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('amount', models.PositiveIntegerField(verbose_name='Increment Amount')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Increment Date')),
            ],
            options={
                'verbose_name': 'Employee Increment',
                'verbose_name_plural': 'Employee Increments',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='IncrementOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Order Creation Date')),
                ('note', models.CharField(max_length=255, verbose_name='Order Note')),
                ('percentage_increment', models.FloatField(verbose_name='Percentage Increment')),
            ],
            options={
                'verbose_name': 'Increment Order',
                'verbose_name_plural': 'Increment Orders',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Leaves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deductions', models.PositiveIntegerField(help_text='Enter the amount to be deducted from payroll for this leave.', verbose_name='Payroll Deduction Amount')),
                ('executive_approval', models.BooleanField(default=False, help_text='Has the executive approved this leave?', verbose_name='Executive Approval')),
                ('leave_date', models.DateField(help_text='Select the start date for the leave.', verbose_name='Leave Start Date')),
                ('leave_end_date', models.DateField(help_text='Select the end date for the leave.', verbose_name='Leave End Date')),
                ('note', models.TextField(blank=True, help_text='Add any additional notes regarding the leave.', verbose_name='Leave Notes')),
                ('principal_approval', models.BooleanField(default=False, help_text='Has the principal approved this leave?', verbose_name='Principal Approval')),
                ('reason', models.TextField(help_text='Provide a reason for taking the leave.', verbose_name='Reason for Leave')),
                ('request_date', models.DateField(auto_now_add=True, help_text='The date when the leave request was made.', verbose_name='Request Date')),
                ('secretary_approval', models.BooleanField(default=False, help_text='Has the secretary approved this leave?', verbose_name='Secretary Approval')),
                ('status', models.CharField(help_text='Current status of the leave request.', max_length=50, verbose_name='Leave Status')),
                ('vc_approval', models.BooleanField(default=False, help_text='Has the Vice Chancellor approved this leave?', verbose_name='Vice Chancellor Approval')),
            ],
            options={
                'verbose_name': 'Leave',
                'verbose_name_plural': 'Leaves',
                'ordering': ['-request_date'],
            },
        ),
        migrations.CreateModel(
            name='LeaveType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Leave Type Name')),
                ('days_paid', models.PositiveIntegerField(verbose_name='Paid Days Allowed')),
                ('department', models.CharField(max_length=100, verbose_name='Department')),
                ('granted_times_in_service', models.PositiveIntegerField(verbose_name='Total Times Granted')),
                ('granted_times_interval', models.PositiveIntegerField(verbose_name='Grant Interval (Months)')),
            ],
            options={
                'verbose_name': 'Leave Type',
                'verbose_name_plural': 'Leave Types',
            },
        ),
        migrations.CreateModel(
            name='PayStructure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('annual_increment', models.IntegerField(help_text='Enter the annual increment amount.', verbose_name='Annual Increment')),
                ('basic_pay', models.IntegerField(help_text='Enter the basic pay amount.', verbose_name='Basic Pay')),
                ('conveyance_allowance', models.IntegerField(help_text='Enter the conveyance allowance amount.', verbose_name='Conveyance Allowance')),
                ('hra', models.IntegerField(help_text='Enter the house rent allowance amount.', verbose_name='House Rent Allowance (HRA)')),
                ('medical_allowance', models.IntegerField(help_text='Enter the medical allowance amount.', verbose_name='Medical Allowance')),
                ('employee_designation', models.ForeignKey(help_text='Select the designation related to this pay structure.', on_delete=django.db.models.deletion.CASCADE, related_name='pay_structures', to='employee.employeedesignation', verbose_name='Employee Designation')),
            ],
            options={
                'verbose_name': 'Pay Structure',
                'verbose_name_plural': 'Pay Structures',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('annual_increments', models.FloatField(verbose_name='Annual Increments')),
                ('arrears', models.PositiveIntegerField(verbose_name='Arrears')),
                ('conveyance_allowance', models.PositiveIntegerField(verbose_name='Conveyance Allowance')),
                ('cp_fund', models.PositiveIntegerField(verbose_name='CP Fund')),
                ('date_issued', models.DateField(verbose_name='Date Issued')),
                ('education_allowance', models.PositiveIntegerField(verbose_name='Education Allowance')),
                ('employee_oldage_benefit_inst', models.PositiveIntegerField(verbose_name='Old-Age Benefit')),
                ('eobi', models.PositiveIntegerField(verbose_name='EOBI')),
                ('house_rent_allowance', models.PositiveIntegerField(verbose_name='House Rent Allowance')),
                ('inc_aug_15_allowance', models.PositiveIntegerField(verbose_name="Aug '15 Increment Allowance")),
                ('inc_aug_17_svc_allowance', models.PositiveIntegerField(verbose_name="Aug '17 Service Allowance")),
                ('inc_sep_21_svc_allowance', models.PositiveIntegerField(verbose_name="Sep '21 Service Allowance")),
                ('income_tax', models.PositiveIntegerField(verbose_name='Income Tax')),
                ('increments', models.FloatField(verbose_name='Increments')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Is Paid')),
                ('loan_installment', models.FloatField(verbose_name='Loan Installment')),
                ('lowp', models.PositiveIntegerField(verbose_name='Loss of Pay Deduction')),
                ('medical_allowance', models.PositiveIntegerField(verbose_name='Medical Allowance')),
                ('mphil_phd_allowance', models.PositiveIntegerField(verbose_name='MPhil/PhD Allowance')),
                ('pay_roll_no', models.CharField(max_length=255, verbose_name='Payroll Number')),
                ('payment_method', models.CharField(max_length=50, verbose_name='Payment Method')),
                ('security_deposit', models.PositiveIntegerField(verbose_name='Security Deposit')),
                ('spec_head_huntimg_allowance', models.PositiveIntegerField(verbose_name='Special Head-Hunting Allowance')),
                ('svc_allowance', models.PositiveIntegerField(verbose_name='Service Allowance')),
                ('time_generated', models.DateTimeField(auto_now_add=True, verbose_name='Time Generated')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total Amount')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payrolls', to=settings.AUTH_USER_MODEL, verbose_name='Employee')),
                ('employee_pay_structure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payrolls', to='payroll.employeepaystructure', verbose_name='Pay Structure')),
            ],
            options={
                'verbose_name': 'Payroll',
                'verbose_name_plural': 'Payrolls',
                'ordering': ['-date_issued'],
            },
        ),
        migrations.AddConstraint(
            model_name='leavetype',
            constraint=models.UniqueConstraint(fields=('name', 'department'), name='unique_leave_type_per_department'),
        ),
        migrations.AddField(
            model_name='leaves',
            name='deducted_in_payroll',
            field=models.ForeignKey(help_text='Select the payroll record to which this leave is deducted.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leaves_deducted', to='payroll.payroll', verbose_name='Deducted in Payroll'),
        ),
        migrations.AddField(
            model_name='leaves',
            name='employee',
            field=models.ForeignKey(help_text='Select the employee requesting the leave.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_leaves', to=settings.AUTH_USER_MODEL, verbose_name='Employee'),
        ),
        migrations.AddField(
            model_name='leaves',
            name='leave_type',
            field=models.ForeignKey(help_text='Select the type of leave.', on_delete=django.db.models.deletion.CASCADE, related_name='leave_type_leaves', to='payroll.leavetype', verbose_name='Type of Leave'),
        ),
        migrations.AddField(
            model_name='increment',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='increments', to='payroll.incrementorder', verbose_name='Related Increment Order'),
        ),
        migrations.AddField(
            model_name='increment',
            name='pay_structure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='increments', to='payroll.employeepaystructure', verbose_name='Employee Pay Structure'),
        ),
        migrations.AddField(
            model_name='employeepaystructure',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pay_structures', to='employee.employee', verbose_name='Employee'),
        ),
        migrations.AddField(
            model_name='employeepaystructure',
            name='employee_pay_structure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_pay_structures', to='payroll.paystructure', verbose_name='Pay Structure'),
        ),
        migrations.AddField(
            model_name='employeeannualincrement',
            name='employee_structure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='annual_increments', to='payroll.employeepaystructure', verbose_name='Employee Pay Structure'),
        ),
        migrations.AddIndex(
            model_name='paystructure',
            index=models.Index(fields=['employee_designation'], name='payroll_pay_employe_e341dc_idx'),
        ),
        migrations.AddIndex(
            model_name='paystructure',
            index=models.Index(fields=['basic_pay'], name='payroll_pay_basic_p_8a1031_idx'),
        ),
        migrations.AddConstraint(
            model_name='paystructure',
            constraint=models.UniqueConstraint(fields=('employee_designation',), name='unique_pay_structure_per_designation'),
        ),
        migrations.AddIndex(
            model_name='payroll',
            index=models.Index(fields=['employee'], name='payroll_pay_employe_3f4ed2_idx'),
        ),
        migrations.AddIndex(
            model_name='payroll',
            index=models.Index(fields=['date_issued'], name='payroll_pay_date_is_f76dc0_idx'),
        ),
        migrations.AddIndex(
            model_name='payroll',
            index=models.Index(fields=['employee_pay_structure'], name='payroll_pay_employe_fdf2a3_idx'),
        ),
        migrations.AddIndex(
            model_name='payroll',
            index=models.Index(fields=['pay_roll_no'], name='payroll_pay_pay_rol_02e758_idx'),
        ),
        migrations.AddConstraint(
            model_name='payroll',
            constraint=models.UniqueConstraint(fields=('employee', 'date_issued'), name='unique_payroll_per_employee_and_date'),
        ),
        migrations.AddConstraint(
            model_name='payroll',
            constraint=models.UniqueConstraint(fields=('pay_roll_no',), name='unique_payroll_number'),
        ),
        migrations.AddConstraint(
            model_name='leaves',
            constraint=models.UniqueConstraint(fields=('employee', 'leave_date'), name='unique_leave_per_employee_and_date'),
        ),
        migrations.AddConstraint(
            model_name='increment',
            constraint=models.UniqueConstraint(fields=('order', 'pay_structure'), name='unique_increment_per_order_and_pay_structure'),
        ),
        migrations.AddIndex(
            model_name='employeepaystructure',
            index=models.Index(fields=['employee'], name='payroll_emp_employe_3d53b5_idx'),
        ),
        migrations.AddIndex(
            model_name='employeepaystructure',
            index=models.Index(fields=['employee_pay_structure'], name='payroll_emp_employe_7359ef_idx'),
        ),
        migrations.AddConstraint(
            model_name='employeepaystructure',
            constraint=models.UniqueConstraint(fields=('employee', 'employee_pay_structure'), name='unique_employee_pay_structure'),
        ),
        migrations.AddConstraint(
            model_name='employeeannualincrement',
            constraint=models.UniqueConstraint(fields=('employee_structure', 'annual_inc_no'), name='unique_increment_per_employee_structure_and_number'),
        ),
    ]
