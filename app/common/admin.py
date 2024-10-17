# common/admin.py
'''
from django.contrib import admin
from .models import Religion, Nationality, Province

# Admin classes for Religion, Nationality, and Province
class ReligionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class NationalityAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

# Registering the models with the admin site
admin.site.register(Religion, ReligionAdmin)
admin.site.register(Nationality, NationalityAdmin)
admin.site.register(Province, ProvinceAdmin)
'''