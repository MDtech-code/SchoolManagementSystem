# #import uuid
# from django.db import models
# from app.common.models import TimeStampedModel
# from django.contrib.auth.models import User
# from django.utils import timezone
# from app.account.models import CustomUser
# from django_countries.fields import CountryField


# class EmployeeDesignation(TimeStampedModel):
#     department = models.CharField(max_length=255)
#     description = models.TextField()
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name


# class Employee(TimeStampedModel):
#     designation = models.ForeignKey(EmployeeDesignation, on_delete=models.CASCADE)
#     employee_pay_structure = models.ForeignKey('payroll.PayStructure', on_delete=models.CASCADE)
#     account_no = models.CharField(max_length=20)
#     address = models.TextField()
#     bank = models.CharField(max_length=100)
#     city = models.CharField(max_length=50)
#     cnic = models.CharField(max_length=15)
#     contact_no = models.CharField(max_length=11)
#     country = CountryField(blank_label='(select country)') 
   
#     covid_vaccinated = models.BooleanField(default=False)
#     date_of_birth = models.DateField()
#     date_of_joining = models.DateField()
#     date_of_rejoining = models.DateField(null=True, blank=True)
#     date_of_resignation = models.DateField(null=True, blank=True)
#     email = models.EmailField()
#     employee_id = models.CharField(max_length=100)
#     employee_name = models.CharField(max_length=100)
#     employee_status = models.CharField(max_length=20)
#     father_cnic = models.CharField(max_length=15)
#     father_name = models.CharField(max_length=100)
#     gender = models.CharField(max_length=6)
#     is_verified = models.BooleanField(default=False)
#     martial_status = models.CharField(max_length=10)
#     note = models.TextField(null=True, blank=True)
#     province = models.CharField(max_length=50)
#     wing = models.CharField(max_length=50)

#     # def save(self, *args, **kwargs):
#     #     if not self.employee_id:  # Only generate if it's empty
#     #         self.employee_id = f"EMP-{uuid.uuid4().hex[:8].upper()}"  # Generates ID like EMP-XXXXXXX
#     #     super().save(*args, **kwargs)

#     def __str__(self):
#         return self.employee_name

   

# class StaffPerformance(models.Model):
#     employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
#     comments = models.TextField()
#     rating = models.PositiveSmallIntegerField()
#     date_evaluated = models.DateField()

#     def __str__(self):
#         return f"Performance Evaluation for {self.employee.employee_name} on {self.date_evaluated}"
    
# class Qualification(TimeStampedModel):
#     employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="qualifications")
#     discipline = models.CharField(max_length=100)
#     institution = models.CharField(max_length=100)
#     name = models.CharField(max_length=100)
#     year_obtained = models.PositiveIntegerField()

#     def __str__(self):
#          return f"{self.name} - {self.employee.username} ({self.year_obtained})"
    


import uuid
from django.db import models
from app.common.models import TimeStampedModel
from django.contrib.auth.models import User
from django.utils import timezone
from app.account.models import CustomUser



class EmployeeDesignation(TimeStampedModel):
     department = models.CharField(max_length=255)
     description = models.TextField()
     name = models.CharField(max_length=255)

     def __str__(self):
         return self.name


class Employee(TimeStampedModel):
     designation = models.ForeignKey(EmployeeDesignation, on_delete=models.CASCADE)
     employee_pay_structure = models.ForeignKey('payroll.PayStructure', on_delete=models.CASCADE)
     account_no = models.CharField(max_length=20)
     address = models.TextField()
     bank = models.CharField(max_length=100)
     city = models.CharField(max_length=50)
     cnic = models.CharField(max_length=15)
     contact_no = models.CharField(max_length=11)
     country = models.CharField(max_length=50)
     covid_vaccinated = models.BooleanField(default=False)
     date_of_birth = models.DateField()
     date_of_joining = models.DateField()
     date_of_rejoining = models.DateField(null=True, blank=True)
     date_of_resignation = models.DateField(null=True, blank=True)
     email = models.EmailField()
     employee_id = models.CharField(max_length=20, unique=True, blank=True)
     employee_name = models.CharField(max_length=100)
     employee_status = models.CharField(max_length=20)
     father_cnic = models.CharField(max_length=15)
     father_name = models.CharField(max_length=100)
     gender = models.CharField(max_length=6)
     is_verified = models.BooleanField(default=False)
     martial_status = models.CharField(max_length=10)
     note = models.TextField(null=True, blank=True)
     province = models.CharField(max_length=50)
     wing = models.CharField(max_length=50)
     
      
     def save(self, *args, **kwargs):
        if not self.employee_id:
            # Retrieve the last employee with a valid `employee_id` format
            last_employee = (
                Employee.objects.filter(employee_id__regex=r'^EMP\d{4}$')
                .order_by('id')
                .last()
            )
            
            if last_employee and last_employee.employee_id:
                # Extract the numeric part and increment it
                last_id = int(last_employee.employee_id[-4:])
                new_id = f"EMP-{last_id + 1:04}"  # Pads to 4 digits, e.g., EMP0001
            else:
                # Start with EMP0001 if no records exist or if none match the format
                new_id = "EMP-0001"

            self.employee_id = new_id
        
        super().save(*args, **kwargs)

     def __str__(self):
        return f"{self.employee_name} ({self.employee_id})"

    

class StaffPerformance(models.Model):
     employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
     comments = models.TextField()
     rating = models.PositiveSmallIntegerField()
     date_evaluated = models.DateField()

     def __str__(self):
         return f"Performance Evaluation for {self.employee.employee_name} on {self.date_evaluated}"
    
class Qualification(TimeStampedModel):
     employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="qualifications")
     discipline = models.CharField(max_length=100)
     institution = models.CharField(max_length=100)
     name = models.CharField(max_length=100)
     year_obtained = models.PositiveIntegerField()

     def __str__(self):
          return f"{self.name} - {self.employee.username} ({self.year_obtained})"