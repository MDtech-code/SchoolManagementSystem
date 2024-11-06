# from django.contrib.auth.decorators import user_passes_test
# from django.shortcuts import redirect, render

# def role_required(roles):
#     """
#     Decorator to check if the logged-in user has one of the specified roles.
#     Redirects to login if unauthenticated, and to a forbidden page if 
#     authenticated but without the required role.
#     """
#     def decorator(view_func):
#         def _wrapped_view(request, *args, **kwargs):
#             if not request.user.is_authenticated:
#                 return redirect('login')  # Redirect to login if unauthenticated

#             if request.user.role.name not in roles:
#                 # Render a user-friendly forbidden page
#                 return render(request, 'errors/403.html') 

#             return view_func(request, *args, **kwargs)
#         return _wrapped_view
#     return decorator
