# Generated by Django 5.1.1 on 2024-10-20 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_staffattendance'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendance',
            options={'ordering': ['-created_at']},
        ),
    ]
