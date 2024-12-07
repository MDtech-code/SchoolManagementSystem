from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from app.common.models import TimeStampedModel

class Role(TimeStampedModel):
    """
    Represents a role that a user can have (e.g., student, teacher, admin).
    """
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    """
    Extends the default Django User model to include additional fields
    and functionalities.
    """
    role = models.ForeignKey('Role', on_delete=models.SET_NULL,null=True)
    # Add fields for social logins
    google_id = models.CharField(max_length=255, blank=True, null=True)
    facebook_id = models.CharField(max_length=255, blank=True, null=True)
    email_verified = models.BooleanField(default=False)
    token_created_at = models.DateTimeField(null=True,blank=True)
    token_expiry_time = models.DateTimeField(null=True,blank=True)

    def is_token_valid(self):
        if self.token_created_at and self.token_expiry_time:
            return timezone.now() < self.token_expiry_time
        return False


class Profile(TimeStampedModel):
    """
    Stores additional profile information for a user.
    """
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/',default='profile_pics/default_image.jpg')
    bio = models.TextField(blank=True)
    contact_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"Profile for {self.user.username}"

