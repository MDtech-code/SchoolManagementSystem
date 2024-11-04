
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser,Role,Profile

class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg ','placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg','placeholder': 'email'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg','placeholder': 'password'}))
    password2 = forms.CharField(label='Password (again)', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg','placeholder': 'confirm_password'}))
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
# forms.py


# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=150)  # Add a username field
#     password = forms.CharField(widget=forms.PasswordInput)

#     username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


# forms.py

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg ','placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Password'}),label=False)

class ForgetPasswordForm(forms.Form):
    email = forms.EmailField(label="Email Address", required=True, widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email'
        }
    ))


class ResetPasswordForm(forms.Form):
    password = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter new password'})
    )
    confirm_password = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm new password'})
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data




class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio', 'contact_number', 'address']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'