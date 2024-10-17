
from django.db import models
from app.common.models import TimeStampedModel




class Class(TimeStampedModel,models.Model):
    name = models.CharField(max_length=50, unique=True)
    label = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Section(TimeStampedModel,models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    section_of_class = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.section_of_class}-{self.name}"


class Subjects(models.Model):
    subject_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject_type = models.CharField(max_length=64)#choices=SUBJECT_CHOICE, , default=SUBJECT_CHOICE[0][0]
    name = models.CharField(max_length=264)

    def __str__(self):
        return self.name
