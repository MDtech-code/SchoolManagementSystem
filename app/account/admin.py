
from django.contrib import admin
from .models import CustomUser,Role,Profile
admin.site.register(CustomUser)
admin.site.register(Role)
admin.site.register(Profile)
