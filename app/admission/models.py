'''

from django.db import models

class Nationality(models.Model):
   
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


"""class Religion(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
"""

class Class(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    label = models.IntegerField()

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=50)
    class_of_section = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.class_of_section.name}"


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Occupation(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Admission(models.Model):
    admission_no = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=200)
    admission_class = models.ForeignKey(Class, related_name='admission_class', on_delete=models.CASCADE)
    admission_section = models.ForeignKey(Section, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    nationality = models.ForeignKey(Nationality, on_delete=models.SET_NULL, null=True)
    religion = models.ForeignKey(Religion, on_delete=models.SET_NULL, null=True)
    date_of_birth = models.DateField()
    blood_group = models.CharField(max_length=3)
    current_address = models.CharField(max_length=255)
    permanent_address = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField()
    guardian_name = models.CharField(max_length=200)
    guardian_relation = models.CharField(max_length=50)
    guardian_contact = models.CharField(max_length=15)
    guardian_address = models.CharField(max_length=255)
    father_occupation = models.ForeignKey(Occupation, related_name='father_occupation', on_delete=models.SET_NULL, null=True)
    mother_occupation = models.ForeignKey(Occupation, related_name='mother_occupation', on_delete=models.SET_NULL, null=True)
    remarks = models.TextField(blank=True, null=True)
    is_voucher_generated = models.BooleanField(default=False)
    admission_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name
'''