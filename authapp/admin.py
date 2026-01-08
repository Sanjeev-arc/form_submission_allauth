from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile
from .models import Academic_Overview, Today_Schedule, Form_Submission
# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'phone_number', 'date_of_birth')
    search_fields = ('first_name', 'last_name', 'user__username', 'user__email')    

@admin.register(Academic_Overview)
class AcademicOverviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'Current_GPA', 'credits_completed', 'current_semester')
    search_fields = ('user__username', 'user__email', 'current_semester')
@admin.register(Today_Schedule)
class TodayScheduleAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject_name', 'professor_name', 'start_time', 'end_time')
    search_fields = ('user__username', 'user__email', 'subject_name', 'professor_name')

@admin.register(Form_Submission)
class FormSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
    search_fields = ('name', 'email', 'subject')