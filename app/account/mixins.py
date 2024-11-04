from django.shortcuts import redirect

class RedirectAuthenticatedUserMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('redirect_to_dashboard')  # Redirect to dashboard or any other page
        return super().dispatch(request, *args, **kwargs)
