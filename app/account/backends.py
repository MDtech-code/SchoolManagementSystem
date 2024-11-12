
# #! both username and email 
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from app.student.models import Student

User = get_user_model()

class EmailOrUsernameBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Try to get the user by username or email (case-insensitive)
            user = User.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
        except User.DoesNotExist:
            try:
                # If not found by username or email, try by roll_no through Student model
                student = Student.objects.get(roll_no=username)  # Removed __iexact
                user = student.user
            except Student.DoesNotExist:
                # If no student with that roll_no is found, return None
                return None
        except User.MultipleObjectsReturned:
            # Handle the case where multiple users have the same email
            return User.objects.filter(email__iexact=username).order_by('id').first()

        if user.check_password(password):
            return user
        return None
# from django.contrib.auth import get_user_model
# from django.contrib.auth.backends import ModelBackend
# from app.student.models import Student
# User = get_user_model()

# class EmailOrUsernameBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         try:
#             # Try to get the user by username, case-insensitive
#             user = User.objects.get(username__iexact=username) 
#         except User.DoesNotExist:
#             try:
#                 # If not found, try to get the user by email, case-insensitive
#                 user = User.objects.get(email__iexact=username)
#             except User.DoesNotExist:
#                 # If still not found, return None
#                 # If not found by username or email, try by roll_no through Student model
#                 student = Student.objects.get(roll_no__iexact=username)
#                 user = student.user  # Get the associated user
#                 return None
#             except User.MultipleObjectsReturned:
#                 # Handle the case where multiple users have the same email
#                 return User.objects.filter(email__iexact=username).order_by('id').first()

