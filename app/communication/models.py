from django.db import models
from app.common.models import TimeStampedModel
class Message(TimeStampedModel):
    sender = models.ForeignKey('student.Student', on_delete=models.CASCADE)  # Adjust if you have a User model
    receiver = models.ForeignKey('student.Student', on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Message from {self.sender} to {self.receiver}"
class Notification(TimeStampedModel):
    user = models.ForeignKey('student.Student', on_delete=models.CASCADE)  # Adjust as necessary
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    def __str__(self):
        return f"Notification for {self.user}: {self.message}"
