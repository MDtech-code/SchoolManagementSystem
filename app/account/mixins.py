from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin

class RedirectAuthenticatedUserMixin:
    redirect_authenticated_user = True  # Default behavior for mixin

    def dispatch(self, request, *args, **kwargs):
        if self.redirect_authenticated_user and request.user.is_authenticated:
            return redirect('redirect_to_dashboard')  # Ensure this URL is defined
        return super().dispatch(request, *args, **kwargs)




class NotAuthenticatedMixin(UserPassesTestMixin):
    redirect_field_name = None

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect('redirect_to_dashboard')  # Or your desired redirect URL

# from django.shortcuts import redirect

# class RedirectAuthenticatedUserMixin:
#     def dispatch(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return redirect('redirect_to_dashboard')  # Redirect to dashboard or any other page
#         return super().dispatch(request, *args, **kwargs)
