

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

from .models import CustomUser
from .forms import CustomUserForm, LoginForm, ResetPasswordForm
from app.account.utils.generate_Token import generate_verification_token
import jwt



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

'''
# Signup View
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
    success_url = reverse_lazy('employee_list')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')  # Get username instead of email
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            # If authentication fails, re-render form with error
            form.add_error(None, "Invalid username or password")  # Update the error message
            return self.form_invalid(form)

# Logout View
class LogoutView(LoginRequiredMixin, TemplateView):
    template_name = 'logout.html'

    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')
'''
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

# Forget Password View
class ForgetPasswordView(FormView):
    template_name = 'forget_password.html'
    form_class = forms.Form
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        user = CustomUser.objects.filter(email=email).first()
        if user:
            token = generate_verification_token(user.pk)
            reset_link = f"{settings.FRONTEND_URL}/reset_password/?token={token}"
            send_mail(
                'Password Reset Request',
                f"Here is your password reset link: {reset_link}",
                settings.EMAIL_HOST_USER,
                [email],
            )
            return render(self.request, 'email_sent.html', {'message': 'Password reset link has been sent.'})
        return render(self.request, 'forget_password.html', {'error': 'User with this email does not exist.'})

# Reset Password View
class ResetPasswordView(FormView):
    template_name = 'reset_password.html'
    form_class = ResetPasswordForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        token = self.request.GET.get('token')
        new_password = form.cleaned_data.get('password')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user = CustomUser.objects.get(pk=payload['user_id'])
            user.set_password(new_password)
            user.save()
            return redirect('login')
        except (jwt.ExpiredSignatureError, jwt.DecodeError, CustomUser.DoesNotExist):
            return render(self.request, 'reset_password.html', {'error': "Invalid or expired token"})
