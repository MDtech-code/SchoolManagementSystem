from django.db import models
from app.common.models import TimeStampedModel

class Assignment(TimeStampedModel):
    """
    Represents an assignment given to students in a course.
    """
    title = models.CharField(max_length=200, db_index=True)
    description = models.TextField()
    due_date = models.DateTimeField(db_index=True)
    course = models.ForeignKey(
        'academic.Course', on_delete=models.CASCADE, db_index=True
    )
    assignment_type = models.CharField(
        max_length=20,
        choices=[
            ('homework', 'Homework'),
            ('quiz', 'Quiz'),
            ('project', 'Project'),
            ('exam', 'Exam')
        ],
        default='homework'
    )
    # Added for attachments
    attachment = models.FileField(
        upload_to='assignment_attachments/', 
        null=True, 
        blank=True
    ) 

    def __str__(self):
        return self.title


class Submission(TimeStampedModel):
    """
    Represents a student's submission for an assignment.
    """
    assignment = models.ForeignKey(
        Assignment, on_delete=models.CASCADE, db_index=True
    )
    student = models.ForeignKey(
        'student.Student', on_delete=models.CASCADE, db_index=True
    )
    submission_date = models.DateTimeField(auto_now_add=True, db_index=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('submitted', 'Submitted'),
            ('late', 'Late'),
            ('not_submitted', 'Not Submitted')
        ]
    )
    file = models.FileField(upload_to='submissions/')
    grade = models.FloatField(null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.student} - {self.assignment.title}"


class GradingRubric(TimeStampedModel):
    """
    Defines a grading rubric with criteria and points for an assignment.
    """
    assignment = models.ForeignKey(
        Assignment, on_delete=models.CASCADE, db_index=True
    )
    criteria = models.CharField(max_length=255)
    points = models.FloatField()

    def __str__(self):
        return f"{self.criteria} - {self.assignment.title}"
