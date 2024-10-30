# account/middleware.py

from django.shortcuts import redirect
from django.urls import reverse
import re
class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Define paths that don't require authentication
        allowed_paths = [
            reverse('login'),
            reverse('signup'),
            reverse('forget_password'),
            reverse('reset_password'),
            reverse('send_email_verification'),
            reverse('verify_email'),
        ]

         # Add the condition to bypass the default admin path
        if re.match(r'^/admin/', request.path):
            return self.get_response(request)

        # Skip any Django auto-reload paths (such as /__reload__/events/)
        if request.path.startswith('/__reload__/'):
            return self.get_response(request)

        # Check if the user is unauthenticated and not accessing an allowed path
        if not request.user.is_authenticated and request.path not in allowed_paths:
            if request.path != reverse('login'):
                return redirect('login')

        # Continue processing the response if conditions are met
        response = self.get_response(request)
        return response
