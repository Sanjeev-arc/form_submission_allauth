from tkinter.messagebox import IGNORE
from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile
from .models import Academic_Overview, Today_Schedule, Form_Submission, Message_From_CEO, UpcomingDeadlines,Notices
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
    
@admin.register(Message_From_CEO)
class MessageFromCEOAdmin(admin.ModelAdmin):
    list_display=('Ceo_name','message')
    search_fields = ('Ceo_name',)
@admin.register(UpcomingDeadlines)
class UpcomingDeadlinesAdmin(admin.ModelAdmin):
    list_display = ('user', 'Assingment', 'course', 'DueDate', 'status', 'Actions')
    search_fields = ('user__username', 'user__email', 'Assingment', 'course')
    list_filter = ('DueDate', 'status')
@admin.register(Notices)
class NoticesAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'is_active')
    search_fields = ('title', 'message')
    list_filter = ('is_active', 'date_posted')  
    