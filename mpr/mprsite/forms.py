#from allauth.account.forms import SignupForm
from django import forms
from mprsite.models import UserProfile, create_profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from allauth.account.adapter import DefaultAccountAdapter
from django.core.exceptions import ValidationError
from allauth.account.forms	import LoginForm, SignupForm, app_settings
from allauth.account.utils import perform_login

class MySignupForm(SignupForm):
	class Meta:
		model = UserProfile
		grad_year = forms.DecimalField(label=("Graduation Year"), min_value=2016, max_digits=5, decimal_places=1,widget=forms.TextInput())
		fields = ('token_one', 'token_two', 'token_three', 'token_four', 'grad_year')

	grad_year = forms.DecimalField(label=("Graduation Year"), min_value=2016, max_digits=5, decimal_places=1,)

	def signup(self, request, user):
		up = user.userprofile
		up.grad_year = self.cleaned_data['grad_year']
		up.save()

class MyAdapter(DefaultAccountAdapter):
	def clean_email(self, email):
		email_domain = email.split('@')[1]
		if(email_domain != 'middlebury.edu'):
			raise ValidationError(('Invalid value: %(value)s. You must sign up using a valid \'middlebury.edu\' email address.'), code='invalid', params={'value': email},)
		return email

class MyLoginForm(LoginForm):
	def __init__(self, *args, **kwargs):
		super(MyLoginForm, self).__init__(*args, **kwargs)
		login_widget = forms.TextInput(attrs={'type': 'email', 'placeholder': '@middlebury.edu email address', 'autofocus': 'autofocus'})
		forms.EmailField(widget=login_widget)
		#self.fields['login'].widget = forms.TextInput(attrs={'type': 'email', 'class': 'yourclass'})
		#self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'yourclass'})
		#set_form_field_order(self,  ["password", "login", "remember"])
		if 'remember' in self.fields.keys():
			del self.fields['remember']

	def login(self, request, redirect_url=None):
		if not app_settings.EMAIL_VERIFICATION:
			raise ValidationError('You need to confirm your email address before you can login.')

		ret = perform_login(request, self.user,
        					email_verification=app_settings.EMAIL_VERIFICATION,
        					redirect_url=redirect_url)
		'''
		remember = app_settings.SESSION_REMEMBER
		if remember is None:
			remember = self.cleaned_data['remember']
		if remember:
			request.session.set_expiry(app_settings.SESSION_COOKIE_AGE)
		else:
		'''
		request.session.set_expiry(0)
		return ret

