from django.contrib import admin
from .models import Attendance,StaffAttendance

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'is_present')
    list_filter = ('is_present', 'date')
    search_fields = ('student__admission__personal_info__full_name',)

admin.site.register(Attendance, AttendanceAdmin)



@admin.register(StaffAttendance)
class StaffAttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'is_present', 'is_late', 'is_excused')
    search_fields = ('employee__name',)
    list_filter = ('is_present', 'is_late', 'is_excused', 'date')
    date_hierarchy = 'date'
    ordering = ('-date',)

    fieldsets = (
        (None, {
            'fields': ('employee', 'date')
        }),
        ('Attendance Details', {
            'fields': ('is_present', 'is_late', 'is_excused', 'remarks')
        }),
    )