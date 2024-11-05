# Generated by Django 4.2.16 on 2024-10-31 12:14

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0009_merge_20241028_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_id',
            field=models.CharField(editable=False, max_length=20, unique=True),
        ),
    ]