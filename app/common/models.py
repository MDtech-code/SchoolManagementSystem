
# common/models.py
from django.db import models

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class Religion(TimeStampedModel,models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name}"
    

class Nationality(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.title}"
    

class Province(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.title}"
