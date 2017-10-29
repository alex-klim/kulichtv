from django import forms
from .models import *

class CommunityPostForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = '__all__'


class ProfilePostForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
