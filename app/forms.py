from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()


class RegistrationsForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(), required=True)

class EmailVerifacationForm(forms.Form):
    code = forms.CharField(max_length=6, required=True)