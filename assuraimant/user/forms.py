from django import forms
from assuraimant.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email','password']