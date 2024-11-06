from django.contrib import admin

# Register your models here.
from .models import Religion,Nationality,Province,Category

admin.site.register(Religion)
admin.site.register(Nationality)
admin.site.register(Province)
admin.site.register(Category)