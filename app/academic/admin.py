# academic/admin.py

from django.contrib import admin
from .models import Class, Section, Subjects,Department,SchoolLeavingCertificate

@admin.register(SchoolLeavingCertificate)
class SchoolLeavingCertificateAdmin(admin.ModelAdmin):
    list_display = ('student', 'admission_class', 'last_class', 'admission_date', 'leaving_date', 'is_refunded')
    search_fields = ('student__name', 'admission_class__name', 'last_class__name')
    list_filter = ('is_refunded', 'admission_date', 'leaving_date')
    date_hierarchy = 'admission_date'
    ordering = ('-admission_date',)

    fieldsets = (
        (None, {
            'fields': ('student', 'admission_class', 'last_class', 'admission_date', 'leaving_date')
        }),
        ('Financial Information', {
            'fields': ('arrears_remaining', 'is_refunded', 'security_refunded', 'paid_to', 'received_by', 'refund_date')
        }),
        ('Additional Information', {
            'fields': ('remarks',)
        }),
    )
# Admin classes for better presentation
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'label')
    search_fields = ('name',)
    list_filter = ('label',)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

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
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Subjects, SubjectAdmin)

