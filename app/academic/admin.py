# academic/admin.py
'''
from django.contrib import admin
from .models import Class, Section, Subjects
from app.common.models import Religion, Nationality, Province

# Admin classes for better presentation
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'label')
    search_fields = ('name',)
    list_filter = ('label',)

class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'section_of_class')
    search_fields = ('name',)
    list_filter = ('section_of_class',)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject_class', 'subject_type')
    search_fields = ('name', 'subject_class__name')  # Assuming Class has a name field
    list_filter = ('subject_class', 'subject_type')

# Registering the models with the admin site
admin.site.register(Class, ClassAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Subjects, SubjectAdmin)

# Registering models from the common app
admin.site.register(Religion)
admin.site.register(Nationality)
admin.site.register(Province)

'''