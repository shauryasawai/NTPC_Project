from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES)
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'dark-input'}),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'dark-input'}),
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'dark-input', 'help_text': ''}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'dark-input', 'help_text': ''}),
    )
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role', 'password1', 'password2']
