from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    phone_number=models.IntegerField()
    date_of_birth=models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.first_name

class Academic_Overview(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    Current_GPA=models.FloatField()
    credits_completed=models.IntegerField()
    current_semester=models.CharField(max_length=100)
    
    def __str__(self):
        return self.user.username
class Today_Schedule(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    subject_name=models.CharField(max_length=100)
    professor_name=models.CharField(max_length=100)
    start_time=models.TimeField()
    end_time=models.TimeField()
    
    def __str__(self):
        return self.professor_name

class Form_Submission(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(blank=False, null=False)
    subject=models.CharField(max_length=200)        
    message=models.TextField(blank=False, null=False)
    
    def __str__(self):
        return self.name

class Message_From_CEO(models.Model):
    Ceo_name=models.CharField(max_length=100)
    message=models.TextField(blank=False, null=False)
    image=models.ImageField(upload_to='ceo_messages/', null=True, blank=True)
    
    def __str__(self):
        return self.Ceo_name
class UpcomingDeadlines(models.Model):
     user=models.ForeignKey(User, on_delete=models.CASCADE)
     Assingment=models.CharField(max_length=200)
     course=models.CharField(max_length=100)
     DueDate=models.DateField()
     status=models.CharField(max_length=50)
     Actions=models.CharField(max_length=100)
     
     def __str__(self):
         return self.course