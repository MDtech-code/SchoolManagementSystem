
#! both username and email 

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

User = get_user_model()

class EmailOrUsernameBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Try to get the user by username, case-insensitive
            user = User.objects.get(username__iexact=username) 
        except User.DoesNotExist:
            try:
                # If not found, try to get the user by email, case-insensitive
                user = User.objects.get(email__iexact=username)
            except User.DoesNotExist:
                # If still not found, return None
                return None
            except User.MultipleObjectsReturned:
                # Handle the case where multiple users have the same email
                return User.objects.filter(email__iexact=username).order_by('id').first()

        # ... rest of the code remains the same ...

'''
from django.contrib.auth.backends import ModelBackend  # Use ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailOrUsernameBackend(ModelBackend):  # Inherit from ModelBackend
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Try to get the user by username
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            try:
                # If not found, try to get the user by email
                user = User.objects.get(email=username)
            except User.DoesNotExist:
                # If still not found, return None
                return None

        if user.check_password(password):
            return user
        return None
'''
#! only with email 
'''
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Try to get the user by email
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
'''