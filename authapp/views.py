from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from allauth.account.views import SignupView
from allauth.account.forms import app_settings
from .models import UserProfile, Academic_Overview, Today_Schedule, Form_Submission, Message_From_CEO, UpcomingDeadlines
class CustomSignupView(SignupView):
    def form_valid(self,form):
        response=super().form_valid(form)
        if app_settings.EMAIL_VERIFICATION == app_settings.EMAIL_VERIFICATION_MANDATORY:
            messages.success(self.request,' Please check your email to verify your account.')
        else:
            messages.success(self.request,'''Account created successfully! You are now logged in.'''   )
        return response

def home_view(request):
    msg_ceo=Message_From_CEO.objects.all()
    context={
        'msg_ceo':msg_ceo,
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and message:
            Form_Submission.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )

    return render(request, 'authapp/home.html', context=context)

@login_required
def portol_view(request):
    academic = Academic_Overview.objects.filter(user=request.user).first()
    schedule = Today_Schedule.objects.filter(user=request.user).first()
    deadlines=UpcomingDeadlines.objects.filter(user=request.user).all()
    context={
        'academic_overview': academic,
        'schedule': schedule,
        'deadlines': deadlines,
    }

    return render(request, 'authapp/portol.html', context=context)