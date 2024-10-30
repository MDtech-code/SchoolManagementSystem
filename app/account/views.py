

from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.utils import timezone
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from .models import CustomUser
from .forms import CustomUserForm, LoginForm, ResetPasswordForm,ForgetPasswordForm 
from app.account.utils.generate_Token import generate_verification_token
from app.account.utils.decodeVerficationToken import decode_verification_token
import jwt
from django.views import View



class SignupView(FormView):
    template_name = 'signup.html'
    form_class = CustomUserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# Login View
class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('dashboard')
    redirect_authenticated_user = True

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user:
            login(self.request, user)
            return super().form_valid(form)
        form.add_error(None, "Invalid username or password")
        return self.form_invalid(form)

# Logout View
class LogoutView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')
    
# Dashboard View
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'


# Send Email Verification
class SendEmailVerificationView(LoginRequiredMixin, TemplateView):
    template_name = 'verify_email.html'

    def post(self, request):
        user = request.user
        if not user.email_verified:
            token = generate_verification_token(user.pk)
            user.token_created_at = timezone.now()
            user.token_expiry_time = timezone.now() + timezone.timedelta(minutes=30)
            user.save()
            
            verification_link = f"{settings.FRONTEND_URL}/verify_email/?token={token}"
            send_mail(
                'Email Verification Request',
                f"Here is your email verification link: {verification_link}",
                settings.EMAIL_HOST_USER,
                [user.email]
            )
            return redirect('email_sent')
        return redirect('profile')

# Verify Email View
class EmailVerifyView(TemplateView):
    template_name = 'verify_email_result.html'

    def get(self, request, *args, **kwargs):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user = CustomUser.objects.get(pk=payload['user_id'])
            if user.is_token_valid():
                user.email_verified = True
                user.save()
                return render(request, self.template_name, {'message': "Email verified successfully"})
            return render(request, self.template_name, {'message': "Token has expired"})
        except (jwt.ExpiredSignatureError, jwt.DecodeError, CustomUser.DoesNotExist):
            return render(request, self.template_name, {'message': "Invalid token"})

# Send Email Verification
# class SendEmailVerificationView(LoginRequiredMixin, TemplateView):
#     template_name = 'verify_email.html'

#     def post(self, request):
#         user = request.user
#         if not user.email_verified:
#             token = generate_verification_token(user.pk)
#             user.token_created_at = timezone.now()
#             user.token_expiry_time = timezone.now() + timezone.timedelta(minutes=30)
#             user.save()
            
#             verification_link = f"{settings.FRONTEND_URL}/verify_email/?token={token}"
#             send_mail(
#                 'Email Verification Request',
#                 f"Here is your email verification link: {verification_link}",
#                 settings.EMAIL_HOST_USER,
#                 [user.email]
#             )
#             return redirect('email_sent')
#         return redirect('profile')

# # Verify Email View
# class EmailVerifyView(TemplateView):
#     template_name = 'verify_email_result.html'

#     def get(self, request, *args, **kwargs):
#         token = request.GET.get('token')
#         try:
#             payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
#             user = CustomUser.objects.get(pk=payload['user_id'])
#             if user.is_token_valid():
#                 user.email_verified = True
#                 user.save()
#                 return render(request, self.template_name, {'message': "Email verified successfully"})
#             return render(request, self.template_name, {'message': "Token has expired"})
#         except (jwt.ExpiredSignatureError, jwt.DecodeError, CustomUser.DoesNotExist):
#             return render(request, self.template_name, {'message': "Invalid token"})

# Forget Password View
# class ForgetPasswordView(FormView):
#     template_name = 'forget_password.html'
#     form_class = forms.Form
#     success_url = reverse_lazy('login')

#     def form_valid(self, form):
#         email = form.cleaned_data.get('email')
#         user = CustomUser.objects.filter(email=email).first()
#         if user:
#             token = generate_verification_token(user.pk)
#             reset_link = f"{settings.FRONTEND_URL}/reset_password/?token={token}"
#             send_mail(
#                 'Password Reset Request',
#                 f"Here is your password reset link: {reset_link}",
#                 settings.EMAIL_HOST_USER,
#                 [email],
#             )
#             return render(self.request, 'email_sent.html', {'message': 'Password reset link has been sent.'})
#         return render(self.request, 'forget_password.html', {'error': 'User with this email does not exist.'})
class ForgetPasswordView(FormView):
    template_name = 'forget_password.html'
    form_class = ForgetPasswordForm  # Use custom form
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        print(f"Email submitted: {email}")  # Debugging statement

        # Fetch the user
        user = CustomUser.objects.filter(email=email).first()
        if user:
            print("User found with this email.")  # Debugging statement
            token = generate_verification_token(user.pk)
            reset_link = f"{settings.FRONTEND_URL}/reset_password/?token={token}"
            
            # Send email with reset link
            send_mail(
                'Password Reset Request',
                f"Here is your password reset link: {reset_link}",
                settings.EMAIL_HOST_USER,
                [email],
            )
            return render(self.request, 'email_sent.html', {'message': 'Password reset link has been sent.'})
        else:
            print("No user found with this email.")  # Debugging statement
            return render(self.request, 'forget_password.html', {'error': 'User with this email does not exist.'})
# Reset Password View
# class ResetPasswordView(FormView):
#     template_name = 'reset_password.html'
#     form_class = ResetPasswordForm
#     success_url = reverse_lazy('login')

#     def form_valid(self, form):
#         token = self.request.GET.get('token')
#         new_password = form.cleaned_data.get('password')
#         try:
#             payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
#             user = CustomUser.objects.get(pk=payload['user_id'])
#             user.set_password(new_password)
#             user.save()
#             return redirect('login')
#         except (jwt.ExpiredSignatureError, jwt.DecodeError, CustomUser.DoesNotExist):
#             return render(self.request, 'reset_password.html', {'error': "Invalid or expired token"})
class ResetPasswordView(View):
    template_name = 'reset_password.html'

    def get(self, request):
        # Token verification
        token = request.GET.get('token')
        user_id = decode_verification_token(token)  # Extracts user ID from token

        if user_id:
            request.session['reset_user_id'] = user_id
            form = ResetPasswordForm()
            return render(request, self.template_name, {'form': form})
        else:
            return render(request, 'error.html', {'message': 'Invalid or expired token.'})

    def post(self, request):
        form = ResetPasswordForm(request.POST)
        user_id = request.session.get('reset_user_id')

        if not user_id:
            return render(request, 'error.html', {'message': 'Session expired. Try again.'})

        if form.is_valid():
            user = CustomUser.objects.get(pk=user_id)
            password = form.cleaned_data['password']
            user.password = make_password(password)
            user.save()
            
            # Clear session after reset
            del request.session['reset_user_id']
            return redirect(reverse_lazy('login'))
        else:
            return render(request, self.template_name, {'form': form})