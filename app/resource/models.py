from django.db import models
from app.common.models import TimeStampedModel


class ResourceType(TimeStampedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Resource(TimeStampedModel):
    title = models.CharField(max_length=200)
    resource_type = models.ForeignKey(ResourceType, on_delete=models.CASCADE)
    course = models.ForeignKey('academic.Course', on_delete=models.CASCADE)
    file = models.FileField(upload_to='resources/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

