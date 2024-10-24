# Generated by Django 5.1.1 on 2024-10-21 11:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0006_alter_class_options_alter_department_options_and_more'),
        ('admission', '0003_occupation_alter_parentinfo_father_occupation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicinfo',
            name='admission_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admitted_class', to='academic.class'),
        ),
        migrations.AlterField(
            model_name='academicinfo',
            name='admission_no',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='academicinfo',
            name='admission_type',
            field=models.CharField(choices=[('REGULAR', 'Regular'), ('TRANSFER', 'Transfer'), ('RE_ADMISSION', 'Re-Admission')], max_length=50),
        ),
        migrations.AlterField(
            model_name='academicinfo',
            name='enrollment_status',
            field=models.CharField(choices=[('ENROLLED', 'Enrolled'), ('PENDING', 'Pending'), ('WITHDRAWN', 'Withdrawn')], max_length=50),
        ),
        migrations.AlterField(
            model_name='admission',
            name='admission_type',
            field=models.CharField(choices=[('REGULAR', 'Regular'), ('TRANSFER', 'Transfer'), ('RE_ADMISSION', 'Re-Admission')], max_length=64),
        ),
        migrations.AlterField(
            model_name='parentinfo',
            name='father_cnic',
            field=models.CharField(max_length=15, verbose_name='CNIC'),
        ),
        migrations.AlterField(
            model_name='parentinfo',
            name='father_full_name',
            field=models.CharField(max_length=100, verbose_name='Father Full Name'),
        ),
        migrations.AlterField(
            model_name='parentinfo',
            name='guardian_cnic',
            field=models.CharField(max_length=15, verbose_name='CNIC'),
        ),
        migrations.AlterField(
            model_name='parentinfo',
            name='guardian_full_name',
            field=models.CharField(max_length=100, verbose_name='guardian Full Name'),
        ),
        migrations.AlterField(
            model_name='parentinfo',
            name='mother_cnic',
            field=models.CharField(max_length=15, verbose_name='CNIC'),
        ),
        migrations.AlterField(
            model_name='parentinfo',
            name='mother_full_name',
            field=models.CharField(max_length=100, verbose_name='Mother Full Name'),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='blood_group',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=3),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='full_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=10),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='general_health',
            field=models.CharField(choices=[('GOOD', 'Good'), ('FAIR', 'Fair'), ('POOR', 'Poor')], max_length=255),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='immunization',
            field=models.CharField(choices=[('FULLY_VACCINATED', 'Fully Vaccinated'), ('PARTIALLY_VACCINATED', 'Partially Vaccinated'), ('NOT_VACCINATED', 'Not Vaccinated')], max_length=255),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='place_of_birth',
            field=models.CharField(max_length=128),
        ),
    ]
