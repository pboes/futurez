from django import forms
from captcha.fields import CaptchaField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
	contact_name = forms.CharField(required=True,label='username')
	captcha = CaptchaField()


class SignUpForm(UserCreationForm):
	captcha = CaptchaField()

	class Meta:
		model = User
		fields = ('username', 'password1', 'password2', 'captcha')