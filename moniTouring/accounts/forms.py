from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

from .models import MoniTouringUser


class MTUserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MoniTouringUser
        fields = ('username', 'email')
        widgets = {'username': forms.TextInput()}


class MTUserEditForm(forms.ModelForm):
    class Meta:
        model = MoniTouringUser
        fields = ('username', 'first_name', 'last_name', 'email', 'profile_picture')
        exclude = ('password',)
        labels = {
            'username': 'Username:',
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'email': 'Email:',
            'profile_picture': 'Profile Picture:'
        }


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True, "placeholder": "Username"}))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "placeholder": "Password"}))