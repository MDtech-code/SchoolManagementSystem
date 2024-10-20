# Generated by Django 5.1.1 on 2024-10-18 08:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
        ('payroll', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('account_no', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('bank', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('cnic', models.CharField(max_length=20)),
                ('contact_no', models.CharField(max_length=15)),
                ('country', models.CharField(max_length=100)),
                ('covid_vaccinated', models.BooleanField(default=False)),
                ('date_of_birth', models.DateField()),
                ('date_of_joining', models.DateField()),
                ('date_of_rejoining', models.DateField(blank=True, null=True)),
                ('date_of_resignation', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('employee_id', models.CharField(max_length=50)),
                ('employee_name', models.CharField(max_length=255)),
                ('employee_status', models.CharField(max_length=50)),
                ('father_cnic', models.CharField(max_length=20)),
                ('father_name', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=10)),
                ('is_verified', models.BooleanField(default=False)),
                ('martial_status', models.CharField(max_length=50)),
                ('note', models.TextField(blank=True, null=True)),
                ('province', models.CharField(max_length=100)),
                ('wing', models.CharField(max_length=100)),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employeedesignation')),
                ('employee_pay_structure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payroll.paystructure')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
