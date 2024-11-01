from app.common.models import TimeStampedModel
from django.db import models



class Assignment(TimeStampedModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField()
    course = models.ForeignKey('academic.Course', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Submission(TimeStampedModel):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE)
    submission_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('submitted', 'Submitted'), ('late', 'Late'), ('not_submitted', 'Not Submitted')])
    file = models.FileField(upload_to='submissions/')

    def __str__(self):
        return f"{self.student} - {self.assignment.title}"
