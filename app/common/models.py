
# common/models.py
from django.db import models
from core.utils.choices import GENDER_CHOICES,MARITAL_STATUS_CHOICES
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']
'''
class PersonInfo(TimeStampedModel):
    full_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    address = models.TextField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    cnic = models.CharField(max_length=20, blank=True, null=True)
    blood_group = models.CharField(max_length=3, blank=True, null=True)
    father_name = models.CharField(max_length=255, blank=True, null=True)
    marital_status = models.CharField(max_length=15, blank=True, null=True, choices=MARITAL_STATUS_CHOICES)
    
    class Meta:
        abstract = True

'''
class Religion(TimeStampedModel):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name}"
    

class Nationality(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.title}"
    

class Province(TimeStampedModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.title}"



class Category(TimeStampedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name