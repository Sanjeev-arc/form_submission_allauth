from django import forms

from authapp.models import UserProfile
class CustomSignupForm(forms.Form):
    first_name=forms.CharField(max_length=30, label='First Name')
    last_name=forms.CharField(max_length=30, label='Last Name')
    phone_number=forms.IntegerField(label='Phone Number')
    date_of_birth=forms.DateField(label='Date of Birth', widget=forms.SelectDateWidget(years=range(1900, 2026)))
    
    def signup(self,request,user):
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        user.save()

        profile=UserProfile(user=user)
        profile.phone_number=self.cleaned_data.get('phone_number')
        profile.save()