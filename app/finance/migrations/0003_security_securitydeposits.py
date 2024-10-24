# Generated by Django 5.1.1 on 2024-10-18 11:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_qualification_staffperformance'),
        ('finance', '0002_expense_incometaxsession_cpfund_cpfunddeposits_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Security',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deposited_security', models.PositiveIntegerField()),
                ('last_date_submitted', models.DateField()),
                ('total_security', models.PositiveIntegerField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_security', to='employee.employee')),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employee_security', to='employee.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SecurityDeposits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('amount', models.PositiveIntegerField()),
                ('date_paid', models.DateField()),
                ('note', models.CharField(max_length=255)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_security_deposits', to='employee.employee')),
                ('security', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='security_deposits', to='finance.security')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]