
#! forms
from .forms import CustomUserForm, LoginForm, ResetPasswordForm,ForgetPasswordForm ,ProfileForm
#! models 
from .models import CustomUser,Role,Profile
#! django 
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, FormView
from django.views.generic.edit import UpdateView
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.utils import timezone
from django.conf import settings
from django.core.mail import BadHeaderError,send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.views import View
from django.contrib import messages
from django.http import HttpResponseRedirect
#! app
from app.account.utils.generate_Token import generate_verification_token
from app.account.utils.decodeVerficationToken import decode_verification_token
from app.admission.models import Admission 
from app.assignment.models import Assignment,Submission
from app.academic.models import Course

#! third party
import jwt

#! mixins
from .mixins import RedirectAuthenticatedUserMixin,NotAuthenticatedMixin
#! decorator 
from .decorators import role_required





@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if not request.user.email_verified:
        messages.info(request, 'Your email address is not verified. Please verify to access all features.')
    context = {'profile': profile}
    return render(request, 'accounts/profiles/profile.html', context)

class EditProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/profiles/edit_profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return get_object_or_404(Profile, user=self.request.user)



# @role_required('teacher')
@login_required
@role_required(['teacher'])
def teacher_dashboard(request):
    """
    Renders the teacher dashboard with relevant data.
    """
    my_courses = Course.objects.all()  # Example: Fetch all courses
    recent_assignments = Assignment.objects.all()  # Example: Fetch all assignments
    pending_submissions = Submission.objects.filter(
        assignment__course__in=my_courses, status='not_submitted'
    )
    # context = get_teacher_data(request)
    context = {
        'my_courses': my_courses,
        'recent_assignments': recent_assignments,
        'pending_submissions': pending_submissions,
        'announcements': [
            {'message': 'Staff meeting on November 6th.'},
            {'message': 'New curriculum updates available.'}
        ]
    }
    return render(request, 'accounts/dashboards/teacher_dashboard.html', context)




# @role_required('staff')
@login_required
@role_required(['staff'])
def staff_dashboard(request):
    """
    Renders the staff dashboard with relevant data.
    """
    # context = get_staff_data(request)
    context = {
        'tasks': [
            {'name': 'Process payments', 'status': 'Pending'},
            {'name': 'Generate reports', 'status': 'Completed'}
        ],
        'announcements': [
            {'message': 'Payroll processed.'},
            {'message': 'Holiday schedule updated.'}
        ]
    }
    return render(request, 'accounts/dashboards/staff_dashboard.html', context)


class SignupView(RedirectAuthenticatedUserMixin,FormView):
    template_name = 'accounts/authentication/signup.html'
    form_class = CustomUserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()  # Let the form handle the initial save
        default_role = Role.objects.get(name='applicant')
        user.role = default_role
        user.save()
        if not user.email_verified:
            token = generate_verification_token(user.pk)
            user.token_created_at = timezone.now()
            user.token_expiry_time = timezone.now() + timezone.timedelta(minutes=30)
            user.save()
            
            verification_link = f"{settings.FRONTEND_URL}/home/verify_email_result/?token={token}"
            # Try sending the email, handle any potential errors
            try:
                send_mail(
                    'Email Verification Request',
                    f"Please verify your email by clicking the following link: {verification_link}",
                    settings.EMAIL_HOST_USER,
                    [user.email],
                    fail_silently=False,
                )
            except Exception as e:
                # Handle the email sending error
                messages.error(self.request, "Account created but email could not be sent. Contact support.")
                # Log the error if needed
                print(f"Error sending verification email: {e}")
                return super().form_valid(form)
             # Save again to update the role
        messages.success(self.request, 'Account created successfully! Please log in.')
        return super().form_valid(form)
    

# Login View
class LoginView(NotAuthenticatedMixin,FormView):
    template_name = 'accounts/authentication/login.html'
    form_class = LoginForm
    # success_url = reverse_lazy('student_dashboard')
    success_url = reverse_lazy('redirect_to_dashboard')
    redirect_authenticated_user = True

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user:
            login(self.request, user)
            if user.is_staff:
                return redirect('/admin/') 
            messages.success(self.request, f'Welcome, {user.username}!')
            #return redirect(self.get_success_url())
            return super().form_valid(form)
        else:
            messages.error(self.request, "Invalid username or password.")
            # form.add_error(None, "Invalid username or password")
            return self.form_invalid(form)

# Logout View
class LogoutView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')


# Send Email Verification
class SendEmailVerificationView( TemplateView):
    template_name = 'accounts/authentication/verify_email.html'

    def post(self, request):
        user = request.user
        if not user.email_verified:
            token = generate_verification_token(user.pk)
            user.token_created_at = timezone.now()
            user.token_expiry_time = timezone.now() + timezone.timedelta(minutes=30)
            user.save()
            
            verification_link = f"{settings.FRONTEND_URL}/home/verify_email_result/?token={token}"
            try:
                send_mail(
                    'Email Verification Request',
                    f"Here is your email verification link: {verification_link}",
                    settings.EMAIL_HOST_USER,
                    [user.email],
                    fail_silently=False,  # Raise exceptions for email errors
                )
                messages.success(self.request, 'Password reset link has been sent to your email.')
                #return HttpResponseRedirect(self.get_success_url())  # Redirect after successful email
                return redirect('profile')
            except BadHeaderError:
                  messages.error(self.request, 'Invalid header found.')
            except Exception as e:  # Catch other email sending errors
                  messages.error(self.request, f'Error sending email: {e}')
        return redirect('profile')

# Verify Email View
class EmailVerifyView(TemplateView):
    template_name = 'accounts/authentication/verify_email_result.html'

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

class ResetPasswordView(View):
    template_name = 'accounts/authentication/reset_password.html'

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
            messages.success(request, 'Password reset successfully!')
            # Clear session after reset
            del request.session['reset_user_id']
            return redirect(reverse_lazy('login'))
        else:
            return render(request, self.template_name, {'form': form})
        



@login_required
def redirect_to_dashboard(request):
    # Check if the user has a role and role has a name
    if hasattr(request.user, 'role') and hasattr(request.user.role, 'name'):
        # Role to dashboard mapping
        role_to_dashboard = {
            'student': 'student_dashboard',
            'teacher': 'teacher_dashboard',
            'staff': 'staff_dashboard',
            'applicant': 'applicant_dashboard',
            # ... add other roles as needed ...
        }

        # Get the dashboard URL based on role
        dashboard_url = role_to_dashboard.get(request.user.role.name)
        if dashboard_url:
            return redirect(dashboard_url)

    # Default redirect if no role or no matching role
    return redirect('home')


def home(request):
    context = {
        'school_name': 'Army Public School',
        'about_school': 'Army Public School is a renowned educational institution committed to providing quality education and holistic development to students. We offer a comprehensive curriculum, experienced faculty, and state-of-the-art facilities to foster academic excellence and personal growth.',
        'admission_info': {
            'open': True,
            'last_date': '2024-12-15',
            'classes': 'Pre-Nursery to 12th Grade',
            'process': 'Visit the school office to obtain an admission form. Submit the completed form along with the required documents by the last date.',
            'contact': 'Call us at +92-XXX-XXXXXXX or email us at admissions@aps.edu.pk for any inquiries.'
        },
        'upcoming_events': [
            {'name': 'Open House', 'date': '2024-11-10'},
            {'name': 'Annual Day', 'date': '2024-12-20'}
        ],
        'testimonials': [
            {'quote': 'Army Public School has provided my child with an excellent learning environment. The teachers are dedicated, and the facilities are top-notch.', 'author': 'Parent of a 5th Grader'},
            {'quote': 'I am grateful for the opportunities and support I received at Army Public School. It helped me achieve my academic goals and prepared me for the future.', 'author': 'APS Alumnus'}
        ]
    }
    return render(request, 'home/home.html',context)



@login_required
@role_required(['applicant'])
def applicant_dashboard(request):
    try:
        admission = Admission.objects.get(applicant=request.user)
    except Admission.DoesNotExist:
        admission = None

    context = {'admission': admission}
    return render(request, 'admission/applicant_dashboard.html', context)
























class ForgetPasswordView(NotAuthenticatedMixin,FormView):
    template_name = 'accounts/authentication/forget_password.html'
    form_class = ForgetPasswordForm  # Use custom form
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        try:
            user = CustomUser.objects.get(email=email)  # Use get() to raise an exception if not found
        except CustomUser.DoesNotExist:
            messages.error(self.request, 'User with this email does not exist.')
            return self.form_invalid(form)  # Or render an error page

        token = generate_verification_token(user.pk)
        reset_link = f"{settings.FRONTEND_URL}/home/reset_password/?token={token}"

        try:
            send_mail(
                'Password Reset Request',
                f"Here is your password reset link: {reset_link}",
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,  # Raise exceptions for email errors
            )
            messages.success(self.request, 'Password reset link has been sent to your email.')
            return HttpResponseRedirect(self.get_success_url())  # Redirect after successful email
        except BadHeaderError:
            messages.error(self.request, 'Invalid header found.')
            return self.form_invalid(form)
        except Exception as e:  # Catch other email sending errors
            messages.error(self.request, f'Error sending email: {e}')
            return self.form_invalid(form)