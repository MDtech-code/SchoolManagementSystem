# from app.common.models import TimeStampedModel
# from app.assignment.models import Assignment
# from django.db import models

# class Grade(TimeStampedModel):
#     student = models.ForeignKey('student.Student', on_delete=models.CASCADE)
#     assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
#     score = models.FloatField()
#     comments = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return f"{self.student} - {self.assignment.title} - {self.score}"

# class Gradebook(TimeStampedModel):
#     course = models.ForeignKey('academic.Course', on_delete=models.CASCADE)
#     grades = models.ManyToManyField(Grade)

#     def __str__(self):
#         return f"Gradebook for {self.course}"
