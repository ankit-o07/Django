from django.forms import ModelForm

from .models import UserProfile
class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ["firstName","lastName","Dob","gender","email","phoneNumber","account_type","userName","password"]