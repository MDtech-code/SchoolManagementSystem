from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect, render

def role_required(roles):
    """
    Decorator to check if the logged-in user has one of the specified roles.
    Redirects to login if unauthenticated, and to a forbidden page if 
    authenticated but without the required role.
    """
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')  # Redirect to login if unauthenticated

            if request.user.role.name not in roles:
                # Render a user-friendly forbidden page
                return render(request, 'errors/403.html') 

            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

# from django.contrib.auth.decorators import user_passes_test
# from django.shortcuts import redirect

# def role_required(roles):
#     """
#     Decorator to check if the logged-in user has one of the specified roles.
#     """
#     def decorator(view_func):
#         def check_role(user):
#             if not user.is_authenticated:
#                 return False
#             return user.role.name in roles

#         actual_decorator = user_passes_test(check_role, login_url='login')
#         return actual_decorator(view_func)
#     return decorator











# from django.core.exceptions import PermissionDenied

# def role_required(role):
#     def decorator(view_func):
#         def _wrapped_view(request, *args, **kwargs):
#             if request.user.role == role:
#                 return view_func(request, *args, **kwargs)
#             raise PermissionDenied  # Return 403 error if role does not match
#         return _wrapped_view
#     return decorator


# from django.core.exceptions import PermissionDenied
# from functools import wraps

# def role_required(role):
#     def decorator(view_func):
#         @wraps(view_func)
#         def _wrapped_view(request, *args, **kwargs):
#             user_role = getattr(request.user, 'role', None)
#             print(f"Expected role: {role}, User role: {user_role}")  # Debugging statement
            
#             if user_role == role:
#                 return view_func(request, *args, **kwargs)
#             raise PermissionDenied("You do not have the required role to access this page.")  # 403 error if role does not match
#         return _wrapped_view
#     return decorator
