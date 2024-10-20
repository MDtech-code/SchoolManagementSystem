# Generated by Django 5.1.1 on 2024-10-18 11:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0004_delete_subjects'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('subject_type', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=264)),
                ('subject_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.class')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
