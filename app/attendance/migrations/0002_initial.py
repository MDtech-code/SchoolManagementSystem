# Generated by Django 4.2.16 on 2024-11-06 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
        ('attendance', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffattendance',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student'),
        ),
    ]
