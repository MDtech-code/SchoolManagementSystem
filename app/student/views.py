# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views import View

# # Create your views here.
# class StudentView(View):
#     def get(self,request):
#         return render(request,'student.html')

from django.contrib.auth.decorators import login_required
from app.account.decorators import role_required
from django.shortcuts import render
from app.assignment.models import Submission
from app.academic.models import Course
@login_required
@role_required(['student'])
def student_dashboard(request):
    """
    Renders the student dashboard with relevant data.
    """
    # context = get_student_data(request)
    upcoming_events = [
        {'name': 'Assignment 1', 'date': '2024-11-10'},
        {'name': 'Exam 1', 'date': '2024-11-15'}
    ]
    announcements = [
        {'message': 'School will be closed on November 5th.'},
        {'message': 'New library books are available.'}
    ]
    # Assuming you have models for grades and assignments
    recent_grades = Submission.objects.filter(student=request.user.id)
    # ... (fetch other data: my_courses, attendance_summary) ...
    context = {
        'upcoming_events': upcoming_events,
        'announcements': announcements,
        'recent_grades': recent_grades,
        'my_courses': Course.objects.all(),  # Example: Fetch all courses
        'attendance_summary': {'present': 20, 'absent': 2}  # Replace with actual data
    }
    return render(request, 'accounts/dashboards/student_dashboard.html', context)


